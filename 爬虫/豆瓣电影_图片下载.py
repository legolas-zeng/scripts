# coding=utf-8
# @Time    : 2019/12/24 16:48
# @Author  : zwa

import re
import requests
import time
import shutil

headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def getPage(get_url):
    r=requests.get(get_url,headers=headers)
    response = r.text
    return response

def filterpage():
    pageCode = getPage(get_url)
    pattern = re.compile('<img width="100" alt="(.*?)" src="(.*?)" class="">',re.S)
    items = re.findall(pattern,pageCode)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(),item[1].strip()])
    return download_image(pageStories)

def download_image(pageStories):
    image_path = "C:\\Users\\Administrator.000\Desktop\images"
    for i in range(25):
        temp = image_path + '/%s.jpg' % pageStories[i][0]
        print('正在下载图片%s' % pageStories[i][0])
        imgurl = pageStories[i][1]
        r = requests.get(imgurl, stream=True)
        if r.status_code == 200:
            with open(temp, 'wb') as f:
                f.write(r.content)
                # r.raw.decode_content = True
                # shutil.copyfileobj(r.raw, f)


if __name__ == '__main__':
    get_url = 'https://movie.douban.com/top250/'
    i=0
    start_time = time.time()
    while i < 11:
        print('--------------正在下载第%s页的图片--------------' % i)
        filterpage()
        num = i * 25
        get_url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        i = i + 1
    end_time = time.time()
    print('总共用时：', end_time - start_time)

