# -*- coding: UTF-8 -*-
import requests,re

def getPage(url):
    r=requests.get(url)
    response = r.text
    return response

def filterpage(url):
    pageCode = getPage(url)
    print(pageCode)
    pattern = re.compile('<a title="(.*?)" href=.*?</a>.*?<img src="(.*?)" />',re.S)
    items = re.findall(pattern, pageCode)
    # items = re.findall(r'<img src="(.*?)" />', pageCode,flags=re.DOTALL )  # re.DOTALL if multi line
    print(items)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(),item[1].strip()])
    return pageStories

url = "http://www.fanpublish.info/2256/page/85"

info = filterpage(url)
print(info)