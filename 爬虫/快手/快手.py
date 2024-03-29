#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: lenovo by XYF
@file: crawl.py
@time: 2020/02/20
@function:
"""

import requests
import json
import time
import os
from bs4 import BeautifulSoup
import re

profile_url = "https://live.kuaishou.com/profile/"
page_url = "https://live.kuaishou.com/m_graphql"
work_url = "https://live.kuaishou.com/u/"

param_did = "?did=web_d374c1dfd56248fb412e64155a5b5b28"

headers = {
    'accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Host': 'live.kuaishou.com',
    'Origin': 'https://live.kuaishou.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',

    # User-Agent 根据自己的电脑修改
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Cookie': 'clientid=3; did=web_d374c1dfd56248fb412e64155a5b5b28; kuaishou.live.bfb1s=ac5f27b3b62895859c4c1622f49856a4; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1600830093; userId=1717892941; didv=1600915340062; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAT9sIiitaMqwtVO_YIZIlEIB6cMF6tfvg4q6Mq1OQH_-CZmHXx3KSnX3hF2JkgTnzrIBLbyJjE9pxeYcdAtgxDvgldGxnpz4so-e3S_uhXNanpD_0Ztz_YyY0QTqcS1k1n7fMopXVWgySYDBhXu7GVcfdMQwljCt4F-HSiOeFI_2gWljinbXnm79HMVsSIszOt9CWuH-ig-z0JurvpoYoCwaEmnXnVZLQknasAunBdtUcHpFQSIgvxN9X_L1EglngJTC3J8rTpqGzTRBzg2bWoBNRF1LkBIoBTAB; kuaishou.live.web_ph=f09fbe843cd35c3cd56230248eeea87d6e2a; userId=1717892941; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1600940012'
}

def crawl_user(uid):
    global headers
    payload = {"operationName": "privateFeedsQuery",
               "variables": {"principalId": uid, "pcursor": "", "count": 999},
               "query": "query privateFeedsQuery($principalId: String, $pcursor: String, $count: Int) {\n  privateFeeds(principalId: $principalId, pcursor: $pcursor, count: $count) {\n    pcursor\n    list {\n      id\n      thumbnailUrl\n      poster\n      workType\n      type\n      useVideoPlayer\n      imgUrls\n      imgSizes\n      magicFace\n      musicName\n      caption\n      location\n      liked\n      onlyFollowerCanComment\n      relativeHeight\n      timestamp\n      width\n      height\n      counts {\n        displayView\n        displayLike\n        displayComment\n        __typename\n      }\n      user {\n        id\n        eid\n        name\n        avatar\n        __typename\n      }\n      expTag\n      __typename\n    }\n    __typename\n  }\n}\n"}
    res = requests.post(page_url, headers=headers, json=payload)

    works = json.loads(res.content.decode(encoding='utf-8', errors='strict'))['data']['privateFeeds']['list']

    if not os.path.exists("data"):
        os.makedirs("data")

    # 这两行代码将response写入json供分析
    # with open("data/" + uid + ".json", "w") as fp:
    #     fp.write(json.dumps(works, indent=2))

    # 防止该用户在直播，第一个作品默认为直播，导致获取信息为NoneType
    if works[0]['id'] is None:
        works.pop(0)
    name = works[0]['user']['name']

    dir = "data/" + name + "(" + uid + ")/"
    # print(len(works))
    if not os.path.exists(dir):
        os.makedirs(dir)
    print("开始爬取用户 " + name + "，保存在目录 " + dir)
    print(" 共有" + str(len(works)) + "个作品")

    for j in range(len(works)):
        crawl_work(uid, dir, works[j], j + 1)
        time.sleep(1)
    print("用户 " + name + "爬取完成!")
    print()
    time.sleep(1)


'''
快手分为五种类型的作品，在作品里面表现为workType属性
 * 其中两种图集: `vertical`和`multiple`，意味着拼接长图和多图，所有图片的链接在imgUrls里
 * 一种单张图片: `single` 图片链接也在imgUrls里
 * K歌: `ksong` 图片链接一样，不考虑爬取音频...
 * 视频: `video` 需要解析html获得视频链接
'''


def crawl_work(uid, dir, work, wdx):
    w_type = work['workType']
    w_caption = re.sub(r"\s+", " ", work['caption'])
    w_name = re.sub(r'[\\/:*?"<>|\r\n]+', "", w_caption)[0:24]
    w_time = time.strftime('%Y-%m-%d', time.localtime(work['timestamp'] / 1000))

    if w_type == 'vertical' or w_type == 'multiple' or w_type == "single" or w_type == 'ksong':
        w_urls = work['imgUrls']
        l = len(w_urls)
        print("  " + str(wdx) + ")图集作品：" + w_caption + "，" + "共有" + str(l) + "张图片")
        for i in range(l):
            p_name = w_time + "_" + w_name + "_" + str(i + 1) + ".jpg"
            pic = dir + p_name
            if not os.path.exists(pic):
                r = requests.get(w_urls[i])
                r.raise_for_status()
                with open(pic, "wb") as f:
                    f.write(r.content)
                print("    " + str(i + 1) + "/" + str(l) + " 图片 " + p_name + " 下载成功 √")
            else:
                print("    " + str(i + 1) + "/" + str(l) + " 图片 " + p_name + " 已存在 √")
    elif w_type == 'video':
        w_url = work_url + uid + "/" + work['id'] + param_did
        print("请求地址：",w_url)
        res = requests.get(w_url, headers=headers)
        html = res.text
        print(html)
        soup = BeautifulSoup(html, "html.parser")

        pattern = re.compile(r"playUrl", re.MULTILINE | re.DOTALL)
        script = soup.find("script", text=pattern)
        s = pattern.search(script.text).string
        v_url = s.split('playUrl":"')[1].split('.mp4')[0].encode('utf-8').decode('unicode-escape') + '.mp4'
        print("  " + str(wdx) + ")视频作品：" + w_caption)
        v_name = w_time + "_" + w_name + ".mp4"
        video = dir + v_name

        if not os.path.exists(video):
            r = requests.get(v_url)
            r.raise_for_status()

            with open(video, "wb") as f:
                f.write(r.content)
            print("视频地址：",v_url)
            print("无水印地址：",noshuiyin(v_url))

            print("    视频 " + v_name + " 下载成功 √")
        else:
            print("    视频 " + v_name + " 已存在 √")
    else:
        print("错误的类型")

def noshuiyin(url: str) -> dict:
    """
    title、imgs、videos
    """
    data = {}
    failed = {'msg': 'failed...'}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
        "Cookie": "did=web_d374c1dfd56248fb412e64155a5b5b28;"
    }
    # rewrite desktop url
    temp = re.findall(r'live\.kuaishou\.com/u/\w+/(\w+)', url)
    print(temp)
    if temp:
        url = 'https://c.kuaishou.com/fw/photo/{}'.format(temp[0])

    rep = requests.get(url, headers=headers, timeout=10)
    if rep.status_code != 200:
        return failed
    page_data = re.findall(r'<script type="text/javascript">window\.pageData= (\{.*?\})</script>', rep.text)
    print(page_data)
    if not page_data:
        return failed
    try:
        page_data = json.loads(page_data[0])
    except Exception:
        print('kuaishou loads json failed')
        return failed

    video_info = page_data['video']
    data['title'] = video_info['caption']
    # 获取视频
    try:  # 如果出错，则可能是长图视频
        data['videos'] = [video_info['srcNoMark']]
    except Exception:
        pass
    else:
        data['videoName'] = data['title']
        data['msg'] = '如果快手视频下载出错请尝试更换网络'
    # 获取图片
    try:  # 如果出错，则可能是普通视频；
        images = video_info['images']
        imageCDN: str = video_info['imageCDN']
        # 如果是长图视频，则这几项一定存在
        assert images is not None
        assert imageCDN is not None
    except Exception:
        pass
    else:
        if not imageCDN.startswith('http'):
            imageCDN = 'http://' + imageCDN
        data['imgs'] = [imageCDN + i['path'] for i in images]
    return data


def read_preset():
    p_path = "preset"
    u_arr = []
    if not os.path.exists(p_path):
        print("创建预设文件 preset ...")
        open(p_path, "w")
    if not os.path.getsize(p_path):
        print("请在预设文件 preset 中记录需要爬取的用户id，一行一个")
        exit(0)
    with open(p_path, "r") as f:
        for line in f:
            if line[0] != "#":
                u_arr.append(line.strip())
    return u_arr


def crawl():
    for uid in read_preset():
        crawl_user(uid)


if __name__ == "__main__":
    crawl()