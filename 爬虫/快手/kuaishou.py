# coding=utf-8
import json
import re
import requests

# TODO 可以用

def get(url: str) -> dict:
    """
    title、imgs、videos
    """
    data = {}
    failed = {'msg': 'failed...'}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
        "Cookie": "did=web_8b1ef0506c146c24627a858c9a646ad2;"
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


if __name__ == "__main__":
    # print(get(url="https://live.kuaishou.com/u/kissyou696773/3x9vpmn3n4ihvg6"))
    print(get(url="https://v.kuaishou.com/6FXp0H"))
    # print(get(url="https://v.kuaishou.com/7CmagI"))
    # from pprint import pprint
    # pprint(get(input("url: ")))