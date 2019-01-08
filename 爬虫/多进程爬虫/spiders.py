# -*- coding: UTF-8 -*-
import urllib.request as request
from bs4 import BeautifulSoup as bs
import asyncio,re
import aiohttp


urlbase = "http://www.fanpublish.info/2256/page/"
page_urls = ["http://www.fanpublish.info/2256/page/85","http://www.fanpublish.info/2256/page/86"]


@asyncio.coroutine
async def getPage(url,res_list):
    print(url)
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    # conn = aiohttp.ProxyConnector(proxy="http://127.0.0.1:8087")
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            assert resp.status==200
            res_list.append(await resp.text())


class parseListPage():
    def __init__(self,page_str):
        self.page_str = page_str
    def __enter__(self):
        page_str = self.page_str
        page = bs(page_str,'lxml')
        # 获取文章链接
        a = str(page)
        pattern = re.compile('<a title="(.*?)" href=.*?</a>.*?<img src="(.*?)" />',re.S)
        items = re.findall(pattern, a)
        print("匹配结果：=======",items)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip()])
        print(pageStories)
        # articles = page.find_all('div',attrs={'class':'article_title'})
        # art_urls = []
        # for a in articles:
        #     x = a.find('a')['href']
        #     art_urls.append('http://blog.csdn.net'+x)
        return pageStories
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


page_num = 5
page_url_base = 'http://www.fanpublish.info/2256/page/'
page_urls = [page_url_base + str(i+1) for i in range(page_num)]
print(page_urls)
loop = asyncio.get_event_loop()
ret_list = []
tasks = [getPage(host,ret_list) for host in page_urls]
loop.run_until_complete(asyncio.wait(tasks))

articles_url = []
print(ret_list)
for ret in ret_list:
    with parseListPage(ret) as tmp:
        articles_url += tmp
ret_list = []

tasks = [getPage(url, ret_list) for url in articles_url]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
