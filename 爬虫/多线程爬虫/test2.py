# -*- coding: UTF-8 -*-
import asyncio,requests,shutil
import aiohttp
import async_timeout
import re
import time
import random
import urllib
from urllib import request
#import uvloop
#asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
def is_in_queue(item,q):
    if item in q:
        return True
    else:
        return False
async def run(url,urlq,kwdq2):
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    try:
        async with aiohttp.ClientSession() as session:
            with async_timeout.timeout(3):
                async with session.get(url,headers=headers) as response:
                    res=await response.text(encoding='utf-8')
                    keywords=re.findall(r'<a title="(.*?)" href=.*?</a>.*?<img src="(.*?)" />',res,re.S)
                    print(keywords)
                    for keyword in keywords:
                        image_path = "C:\\Users\Administrator\Desktop\images"
                        temp = image_path + '/%s.jpg' % keyword[0]
                        image_url = keyword[1]
                        print(u'正在下载图片%s' % image_url)
                        r = requests.get(image_url, stream=True)
                        if r.status_code == 200:
                            with open(temp, 'wb') as f:
                                print('保存图片成功')
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
    except Exception as e :
        print('网页打开失败')
        print(e)
while True:
    url='http://www.fanpublish.info/2256/page/85'
    urlq=[]
    kwdq2=[]
    urlq.append(url)
    while True:
        time_=lambda :time.time()
        start=time_()
        tasks=[]
        count=0
        while count<100:
            if not urlq==[]:
                tempurl=urlq.pop(random.choice(range(0,len(urlq))))  #random.choice(urlq.queue[0]
                print(tempurl)
                tasks.append(asyncio.ensure_future(run(tempurl,urlq,kwdq2)))
            if len(urlq)>10000:
                for i in range(5000):
                    urlq.pop(random.choice(range(len(urlq))))
            if len(kwdq2)>20000:
                for i in range(10000):
                    kwdq2.pop(random.choice(range(len(kwdq2))))
            count+=1
        print('url队列剩余{}'.format(len(urlq)))
        print('****'*20)
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        except:
            print('over')
            break
        print('完成{}个Tasks的时间：{}秒'.format(count,time_()-start))
    print('sleeping..........')
    time.sleep(120)
