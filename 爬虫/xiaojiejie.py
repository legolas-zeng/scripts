# -*-coding:utf-8 -*-
import requests,re
from lxml import etree
from bs4 import BeautifulSoup
import shutil

pagemun = '1563'
url = 'http://www.w24j.com/cn/vl_genre.php?&mode=&g=argq&page=1'

def getPage():
    r=requests.get(url)
    response = r.text
    return response

def filterpage():
    pageCode = getPage()
    pattern = re.compile('<div class="id">(.*?)</div><img src=\"(.*?)\" width=',re.S)
    items = re.findall(pattern, pageCode)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(), item[1].strip()])
    return pageStories
def downloadimage(x,url):
    image_path = 'C:\Users\Administrator\Desktop\images'
    temp = image_path + '/%s.jpg' % x
    print u'正在下载图片%s' % x
    imgurl = 'http:' + url
    print imgurl
    r = requests.get(imgurl, stream=True)
    if r.status_code == 200:
        with open(temp, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

if __name__ == '__main__':
    info = filterpage()
    for data in info:
        x = data[0]
        imgurl = data[1][:-5] + 'l.jpg'
        downloadimage(x,imgurl)

