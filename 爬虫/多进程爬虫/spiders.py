# -*- coding: UTF-8 -*-
import urllib.request as request
from bs4 import BeautifulSoup as bs
import asyncio,re
import aiohttp
import shutil


urlbase = "http://www.fanpublish.info/2256/page/"
page_urls = ["http://www.fanpublish.info/2256/page/85","http://www.fanpublish.info/2256/page/86"]


@asyncio.coroutine
async def getPage(url,res_list):
    print('网页代码：',url)
    # headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    # conn = aiohttp.ProxyConnector(proxy="http://127.0.0.1:8087")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            assert resp.status==200
            res_list.append(await resp.text(encoding='utf-8'))

@asyncio.coroutine
async def download_img(url,res_list):
    print('图片url：',url[1])
    async with aiohttp.ClientSession() as session:
        async with session.get(url[1]) as resp:  # 异步发送请求
            # content = await resp.read()
            # with open("C:\\Users\Administrator\Desktop\images\\"+url[0] + '.jpg', 'wb') as f:
            #     f.write(content)
            # print('下载%s图片成功' % url[0])
            temp = "C:\\Users\Administrator\Desktop\images" + '/%s.jpg' %url[0]
            print(temp)
            with open(temp, 'wb') as f:
                resp.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                print('下载%s图片成功' % url[0])
class parseListPage():
    def __init__(self,page_str):
        self.page_str = page_str
    def __enter__(self):
        page_str = self.page_str
        pattern = re.compile('<a title="(.*?)" href=.*?</a>.*?<img src="(.*?)" />',re.S)
        items = re.findall(pattern, page_str)
        print("匹配结果：=======",items)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip()])
        return pageStories
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


page_num = 1
page_url_base = 'http://www.fanpublish.info/2256/page/'
page_urls = [page_url_base + str(i+1) for i in range(page_num)]
print('page_urls是======：',page_urls)
loop = asyncio.get_event_loop()
ret_list = []
tasks = [getPage(host,ret_list) for host in page_urls]
loop.run_until_complete(asyncio.wait(tasks))

articles_url = []
print(ret_list)
for ret in ret_list:
    with parseListPage(ret) as tmp:
        print("",tmp)
        articles_url += tmp
ret_list = []

tasks = [download_img(url, ret_list) for url in articles_url]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
