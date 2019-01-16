# -*- coding: UTF-8 -*-
import requests
import asyncio
import aiohttp
import random
import sys
import os


def get_proxy():
    resp = requests.get("http://127.0.0.1:5010/get/")
    return resp.text


ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv: 11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
]
base_url = "http://fm.shiyunjj.com/2015/306/{}.jpg"
headers = {
    "Referer": "http://www.mmjpg.com/tag/rosi",
    "User-Agent": random.choice(ua_list),
}


async def get_img(url):
    for i in range(2):
        try:
            filename = url.split("/")[-1]
            # 设置总的请求时长，因为是免费ip，其有效性虽说经过判断有用，但是还是值得商榷的。所以设置了请求总的时长为3秒
            # 默认的是5min，不设置这个，而用免费获得ip，会由于ip的并不有效，而浪费很长时间。
            timeout = aiohttp.ClientTimeout(total=3)
            async with aiohttp.ClientSession(
                    headers=headers, timeout=timeout
            ) as session:
                resp = await session.get(url, proxy="http://" + get_proxy())
                # # 获取响应的头部信息
                # print('resp is ', type(resp.headers['Content-Length']))
                # 若状态码不为200，则下载的不是图片
                # 如若不添加这个判断条件，会出现很多文件存储为图片格式，但是不是图片。。。
                if resp.status != 200:
                    continue
                with open(filename, "wb") as fd:
                    while True:
                        # 这个地方通过对流的处理，而不是一下子整体读取，会更好些
                        # 一下子整个的读取，会导致下载图片的时候，一开始会出现资源浪费，几个协程均处于i/o状态。
                        chunk = await resp.content.read(1024)
                        if not chunk:
                            break
                        fd.write(chunk)
            # 这个是由于，之前下载的图片中一部分，小于正常数值，不是图片。我就通过这种方式判断
            # 起始应该是不需要的，因为加上前面的对状态码的识别，这个部分就应该没问题了
            # if os.path.getsize(filename) != int(resp.headers["Content-Length"]):
            #     # print("{}文件下载不完整,重新下载".format(filename))
            #     continue
            show("{}完成下载".format(filename))
            return
        except asyncio.TimeoutError:
            pass
            # print("第{}次访问网站{}时, 超时".format(url, i+1))
        except aiohttp.client_exceptions.ClientProxyConnectionError:
            pass
            # print("第{}次访问网站{}时, 代理错误".format(url, i+1))
        except Exception as e:
            pass
            # print("第{}次访问网站{}时, {}".format(url, i+1, e.args[0]))
    print("{}未完成下载".format(url))


def show(text):
    print(text)
    sys.stdout.flush()


loop = asyncio.get_event_loop()
to_do = [get_img(base_url.format(cc)) for cc in range(1, 30)]
res, _ = loop.run_until_complete(asyncio.wait(to_do))
loop.close()
