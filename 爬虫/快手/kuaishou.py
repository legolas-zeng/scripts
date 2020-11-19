# coding=utf-8
import json
import re
import requests,os

# TODO 可以用

dir = "H:\\11-快手单个视频\\"
def get(url: str) -> dict:
    """
    title、imgs、videos
    """
    data = {}
    failed = {'msg': 'failed...'}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
        "Cookie": "did=web_f3915064ee334c508642888137f27598;"
    }
    # rewrite desktop url
    temp = re.findall(r'live\.kuaishou\.com/u/\w+/(\w+)', url)
    # print(temp)
    if temp:
        url = 'https://c.kuaishou.com/fw/photo/{}'.format(temp[0])

    rep = requests.get(url, headers=headers, timeout=10)
    if rep.status_code != 200:
        return failed
    page_data = re.findall(r'<script type="text/javascript">window\.pageData= (\{.*?\})</script>', rep.text)
    # print(page_data)
    if not page_data:
        return failed
    try:
        page_data = json.loads(page_data[0])
    except Exception:
        print('kuaishou loads json failed')
        return failed

    video_info = page_data['video']
    data['title'] = video_info['caption']
    # 获取主播名字
    data['user'] = page_data['user']['name']
    # 时间
    data['time'] = page_data['rawPhoto']['timestamp']
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

def readconfig():
    f = open(r'config.txt', "r", encoding='utf-8')
    for x in f:
        geturl(x)
    f.close()

def geturl(config:str)-> list:
    pattern = re.compile(
        '.*?发了一个快手作品，一起来看！(.*?) 复制此消息，打开【快手】直接观看！.*?',
        re.S)
    v_url = re.findall(pattern, config)
    if v_url!= [] :
        req = get(v_url[0])
        download(req)
def download(req):
    v_name = req.get('user') + str(req.get('time')) + ".mp4"
    video = dir + v_name
    print(video)
    print(req.get('videos'))
    if not os.path.exists(video):
        r = requests.get(req.get('videos')[0])
        r.raise_for_status()
        with open(video, "wb") as f:
            f.write(r.content)
        print("    视频 " + v_name + " 下载成功 √")
    else:
        print("    视频 " + v_name + " 已存在 √")
if __name__ == "__main__":
    # print(get(url="https://live.kuaishou.com/u/kissyou696773/3x9vpmn3n4ihvg6"))
    # print(get(url="https://v.kuaishou.com/7x1fql"))
    readconfig()