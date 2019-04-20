# coding=utf-8
# @Time    : 2019/4/18 0:25
# @Author  : zwa
import asyncio,aiohttp,time,re,requests
xls_path = "http://thz8.net/forum-181-1.html"

def getPage():
    get_url='http://thz8.net/forum-181-1.html'
    #top=requests.post(get_url)
    r=requests.get(get_url)
    response = r.text
    return response


def filterpage():
    pageCode = getPage()
    # print(pageCode)
    pattern = re.compile('<a href="(.*?)" style=.*? class="s xst">(.*?)</a>',re.S)
    items = re.findall(pattern,pageCode)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(),item[1].strip()])
    return pageStories

if __name__ == "__main__":
    a = filterpage()
    for data in a:
        print(data)
