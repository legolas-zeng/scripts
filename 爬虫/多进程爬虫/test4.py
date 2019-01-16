import aiohttp
import asyncio
import aiofiles
import async_timeout
from bs4 import BeautifulSoup
import time
import os
import re
import traceback


async def aitaotu(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'Host': 'www.aitaotu.com',
        'Referer': 'https://www.aitaotu.com/guonei/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    }
    async with aiohttp.ClientSession() as session:
        # 列表页
        print('正在访问列表页', url)
        async with session.get(url, verify_ssl=False, headers=headers) as resp:
            if resp.status == 200:
                respdata = await resp.text()
                page = BeautifulSoup(respdata, 'lxml')
                hrefs = page.select('#infinite_scroll > div > div.item_t > div > a')
                titles = page.select('#infinite_scroll > div > div.item_b.clearfix > div.title > span > a')
                for href1, title1 in zip(hrefs, titles):
                    href = href1.get('href')
                    title = title1.get_text()
                    # 内容页
                    href_url = 'https://www.aitaotu.com' + href
                    print('正在访问内容页', href_url)
                    async with session.get(href_url, verify_ssl=False, headers=headers) as contentresp:
                        if contentresp.status == 200:
                            contentrespdata = await contentresp.text()
                            content_page = BeautifulSoup(contentrespdata, 'lxml')
                            m = re.search(r'下一页</a></li><li><a href="(.*?)">末页</a>', contentrespdata)
                            if m:
                                last_page_number = m.group(1).split('.')[0].split('_')[-1]
                                print('内容页', href_url, '总共', last_page_number, '页')
                                # 内容页的所有分页
                                for x in range(1, int(last_page_number) + 1):
                                    newurl = 'https://www.aitaotu.com' + re.sub(r'_([0-9]+).html',
                                                                                '_' + str(x) + '.html', m.group(1))
                                    print('正在访问内容页的分页', newurl)
                                    async with session.get(newurl, verify_ssl=False, headers=headers) as everyresp:
                                        everypagedata = await everyresp.text()
                                        everypage = BeautifulSoup(everypagedata, 'lxml')
                                        images = everypage.select('#big-pic > p > a > img')
                                        for image1 in images:
                                            imageurl = image1.get('src')
                                            print('分页', newurl, '的图片地址', imageurl)
                                            await download_coroutine(imageurl, title)
                                            print('分页{}的图片下载完成'.format(newurl))
            else:
                print('{}被阻止，状态码：'.format(url), resp.status)


async def download_coroutine(imageurl, title):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'Host': 'img.aitaotu.cc:8089',
        'Referer': 'https://www.aitaotu.com/taotu/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(imageurl, verify_ssl=False, headers=headers) as response:
                if not os.path.exists(title):
                    os.mkdir(title)
                filename = os.path.basename(imageurl)
                async with aiofiles.open(os.path.join(title, filename), 'wb') as fd:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await fd.write(chunk)
    except Exception as e:
        traceback.print_exc()


if __name__ == '__main__':
    urllist = ['https://www.aitaotu.com/guonei/list_{}.html'.format(x) for x in range(605)] \
              + ['https://www.aitaotu.com/rihan/list_{}.html'.format(x) for x in range(202)] \
              + ['https://www.aitaotu.com/gangtai/list_{}.html'.format(x) for x in range(33)] \
              + ['https://www.aitaotu.com/meinv/list_{}.html'.format(x) for x in range(89)]
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [aitaotu(url) for url in urllist]
    loop.run_until_complete(asyncio.wait(tasks))
    print('总共耗时 %s s' % (time.time() - start))