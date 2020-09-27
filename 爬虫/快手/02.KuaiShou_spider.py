import os
import re
import sys
import json
import time
import random
import requests
import threading
from queue import Queue
from PyQt5.QtWidgets import (QWidget, QLineEdit,QPushButton,QProgressBar,
                             QTextEdit, QGridLayout, QApplication)
from PyQt5.QtCore import QCoreApplication,pyqtSignal, QThread

cookie = ''
UA_WEB_LIST = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]
UA_AND_LIST = [
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1_r58; zh-cn; MI 6 Build/XPGCG5c067mKE4bJT2oz99wP491yRmlkbGVY2pJ8kELwnF9lCktxB2baBUrl3zdK) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.1_r58; zh-cn; R7Plusm Build/hccRQFbhDEraf5B4M760xBeyYwaxH0NjeMsOymkoLnr31TcAhlqfd2Gl8XGdsknO) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; BLA-AL00 Build/HUAWEIBLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 9)",
    "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.7.34",
]
DID_WEB_LIST = [
    'web_f59491427f0ea183ee1975de99ae1718',
    # 'web_ce554296508e5eac12616081c75f8a27',
    # 'web_027b3637f2aef14cbd14bbf93f50bd4a'
]
DID_AND_LIST = [
    'ANDROID_e0e0ef947bbbc243',
    'ANDROID_1dfef527abefe8c7',
    'ANDROID_5518a3747864010b',
    'ANDROID_25c32123fd766e1e',
    'ANDROID_600b23d707697df0',
    'ANDROID_e1b34c4ac9ddf120',
    'ANDROID_773c33a642ac1845',
    'ANDROID_6a615c268d9dc8d3',
    'ANDROID_c45e742737e83499',
    'ANDROID_c94d28153912d19a',
    'ANDROID_9ba4839bf09a1834',
    'ANDROID_066f7438a673e208'
]
IP_LIST = [
    {"ip": "222.85.28.130", "port": "52590", "type": "HTTP"},
    {"ip": "223.199.27.86", "port": "9999", "type": "HTTP"},
    {"ip": "36.248.132.198", "port": "9999", "type": "HTTP"},
    {"ip": "175.42.123.196", "port": "9999", "type": "HTTP"},
    {"ip": "113.195.168.32", "port": "9999", "type": "HTTP"},
    {"ip": "119.108.165.153", "port": "9000", "type": "HTTP"},
    {"ip": "175.42.158.224", "port": "9999", "type": "HTTP"},
    {"ip": "125.108.114.170", "port": "9000", "type": "HTTP"},
    {"ip": "171.35.169.101", "port": "9999", "type": "HTTP"},
    {"ip": "180.118.128.55", "port": "9000", "type": "HTTP"},
    {"ip": "125.108.79.254", "port": "9000", "type": "HTTP"},
    {"ip": "113.194.130.100", "port": "9999", "type": "HTTP"},
    {"ip": "110.243.27.195", "port": "9999", "type": "HTTP"},
    {"ip": "115.218.214.35", "port": "9000", "type": "HTTP"},
    {"ip": "125.123.152.114", "port": "3000", "type": "HTTP"},
    {"ip": "61.164.39.66", "port": "53281", "type": "HTTP"},
    {"ip": "123.55.98.144", "port": "9999", "type": "HTTP"},
    {"ip": "122.138.141.174", "port": "9999", "type": "HTTP"},
    {"ip": "119.254.94.93", "port": "44665", "type": "HTTP"},
    {"ip": "123.163.27.226", "port": "9999", "type": "HTTP"},
    {"ip": "171.35.170.105", "port": "9999", "type": "HTTP"},
    {"ip": "136.228.128.6", "port": "43117", "type": "HTTP"},
    {"ip": "36.249.48.23", "port": "9999", "type": "HTTP"},
    {"ip": "113.195.21.9", "port": "9999", "type": "HTTP"},
    {"ip": "125.108.73.239", "port": "9000", "type": "HTTP"},
    {"ip": "120.83.107.11", "port": "9999", "type": "HTTP"},
    {"ip": "175.43.156.39", "port": "9999", "type": "HTTP"},
    {"ip": "220.249.149.68", "port": "9999", "type": "HTTP"},
    {"ip": "113.195.18.104", "port": "9999", "type": "HTTP"},
    {"ip": "163.125.30.227", "port": "8118", "type": "HTTP"}
]
PROFILE_URL = "https://live.kuaishou.com/profile/"
DATA_URL = "https://live.kuaishou.com/m_graphql"
WORK_URL = "https://m.gifshow.com/fw/photo/"
USER_ITEM = {}
#后台爬虫
class spider_ks():
    __headers_web = {
        'accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'live.kuaishou.com',
        'Origin': 'https://live.kuaishou.com',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Cookie': 'clientid=3; did=web_d374c1dfd56248fb412e64155a5b5b28; kuaishou.live.bfb1s=ac5f27b3b62895859c4c1622f49856a4; client_key=65890b29; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1600830093; userId=1717892941; didv=1600915340062; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1601115555; kuaishou.live.web_st=ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAZYqa59bfFdQhnlZKwaly8u2g_LVgItiaIBZbvApcjJg3zbQ5KT5tKaPkIDa7ajKYKvg_aGmwZRGOwacnZkup6vSI-nZzkN3_MqsTQNadjhsxwycL4UFIbyy35Uzz9-_fg-JBnKgsOmcwcTmtAY9H__MNYKlp1O05X9hTXqsVLdGN-ofSQ0B49QhjTGSbarU3gidALntkdcZgpIWHSpdREoaEgL1c1j1KEeWrOe8x-vTC5n9jyIg8qsPoa9xXroFaua0XzlxElMUcKsG4V09Y0KBnohH1lYoBTAB; kuaishou.live.web_ph=a1f54ccbc576eb1e978e14c7c9b8f361b109; userId=1717892941'
        # 'Cookie': ''
    }
    __headers_and = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
        'cookie': 'didv=1601199909000; did=web_e669ba67ce5e4dd0b9dc17bcebe067cb; sid=3758ca2a1f17fe5e02c7948c; Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee=1601199868; Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee=1601200116; logj='
    }
    __crawl_list = []
    def __init__(self,satar_url,cookie):
        self.__cookie = cookie
        self.satar_url = ''.join(satar_url.split('\n')).strip()
        self.user_id = None
        self.__crawl_list.append(self.satar_url)
        self.q_works = Queue()
    # 1.爬虫起始
    def spider_start(self):
        print("准备开始爬取，共有%d个用户..." % len(self.__crawl_list))
        for surl in self.__crawl_list:
            self.get_user(surl)
        return True
    # 2.爬取用户个人信息以及作品列表
    def get_user(self, surl):
        proxy_ = random.choice(IP_LIST)
        proxies = {'{}'.format(proxy_['type']): '{0}:{1}'.format(proxy_['ip'], proxy_['port'])}
        self.__headers_web['User-Agent'] = random.choice(UA_WEB_LIST)
        self.__headers_web['Cookie'] = 'did=' + random.choice(DID_WEB_LIST)
        response = requests.get(surl)
        if '/profile/' not in response.request.url:
            uid = response.request.url.split('?')[0].split('/')[-2]
            vid = response.request.url.split('?')[0].split('/')[-1]
            dir_name = './data/'
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            self.get_video_url(uid,vid,dir_name)
            return
        uid = response.request.url.split('/profile/')[-1].split('?')[0]
        self.user_id = uid
        # 获取用户个人信息
        payload = {"operationName": "privateFeedsQuery",
                   "variables": {"principalId": uid, "pcursor": "", "count": 999},
                   "query": "query privateFeedsQuery($principalId: String, $pcursor: String, $count: Int) {\n  privateFeeds(principalId: $principalId, pcursor: $pcursor, count: $count) {\n    pcursor\n    list {\n      id\n      thumbnailUrl\n      poster\n      workType\n      type\n      useVideoPlayer\n      imgUrls\n      imgSizes\n      magicFace\n      musicName\n      caption\n      location\n      liked\n      onlyFollowerCanComment\n      relativeHeight\n      timestamp\n      width\n      height\n      counts {\n        displayView\n        displayLike\n        displayComment\n        __typename\n      }\n      user {\n        id\n        eid\n        name\n        avatar\n        __typename\n      }\n      expTag\n      __typename\n    }\n    __typename\n  }\n}\n"}
        resp = requests.post(DATA_URL, headers=self.__headers_web, json=payload,
                             # proxies=proxies
                             )
        resp.raise_for_status()
        work_list = json.loads(resp.content.decode(encoding='utf-8', errors='strict'))['data']['privateFeeds']['list']

        # 防止该用户在直播，第一个作品默认为直播，导致获取信息为NoneType
        if work_list[0]['id'] is None:
            work_list.pop(0)
        nickname = re.sub(r'[\\/:*?"<>|\r\n]+', "", work_list[0]['user']['name'])
        # 启动另一线程获取并保存用户个人信息
        t = threading.Thread(target=self.get_user_info, args=(uid, work_list,nickname))
        t.start()
        # 构造以昵称(id)为名称的文件夹
        dir_name = "data/" + nickname + "(" + uid + ")/"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        print("开始爬取用户 " + nickname + "，保存在目录 " + dir_name)
        print(" 共有" + str(len(work_list)) + "个作品")

        for i in range(len(work_list)):
            self.q_works.put([dir_name, work_list[i], i + 1])

        t_list = []
        for i in range(50):
            t = threading.Thread(target=self.get_works)
            t.start()
            t_list.append(t)
        for t in t_list:
            t.join()
        print("用户 " + nickname + "爬取完成!")
    # 3.获取视频信息
    def get_works(self):
        while True:
            if self.q_works.qsize() != 0:
                dir_name, work, wk_index = self.q_works.get()
                w_type = work['workType']
                w_caption = re.sub(r"\s+", " ", work['caption'])
                w_name = re.sub(r'[\\/:*?"<>|\r\n]+', "", w_caption)[0:24]
                w_time = time.strftime('%Y-%m-%d', time.localtime(work['timestamp'] / 1000))
                w_index = ""
                if w_type == 'vertical' or w_type == 'multiple' or w_type == "single" or w_type == 'ksong':
                    # 下载图片集
                    w_urls = work['imgUrls']
                    l = len(w_urls)
                    print("  " + str(wk_index) + ")图集作品：" + w_caption + "，" + "共有" + str(l) + "张图片")
                    for i in range(l):
                        p_name = w_time + w_index + "_" + w_name + "_" + str(i + 1) + '.jpg'
                        pic = dir_name + p_name
                        if not os.path.exists(pic):
                            proxy_ = random.choice(IP_LIST)
                            proxies = {'{}'.format(proxy_['type']): '{0}:{1}'.format(proxy_['ip'], proxy_['port'])}
                            r = requests.get(w_urls[i].replace("webp", "jpg"),
                                             # proxies=proxies
                                             )
                            r.raise_for_status()
                            with open(pic, "wb") as f:
                                f.write(r.content)
                            print("    " + str(i + 1) + "/" + str(l) + " 图片 " + p_name + " 下载成功 √")
                        else:
                            print("    " + str(i + 1) + "/" + str(l) + " 图片 " + p_name + " 已存在 √")
                elif w_type == 'video':
                    # 下载视频集
                    vid = work['id']
                    uid = self.user_id
                    self.get_video_url(uid, vid, dir_name,nums=True)
                    try:
                        print("  " + str(wk_index) + ")视频作品：" + w_caption + " 下载成功 √")
                    except:
                        print("  这里似乎有点小错误，已跳过")
                else:
                    print("错误的类型")
                self.q_works.task_done()
            else:
                return
    # 5.获取视频链接并下载
    def get_video_url(self,uid,vid,dir_name,nums=False):
        # print(uid,vid,dir_name)
        proxy_ = random.choice(IP_LIST)
        proxies = {'{}'.format(proxy_['type']): '{0}:{1}'.format(proxy_['ip'], proxy_['port'])}
        self.__headers_and['User-Agent'] = random.choice(UA_AND_LIST)
        did = random.choice(DID_AND_LIST)
        try:
            # 无水印下载链接
            # self.__headers_and['Cookie'] = 'did=' + did
            self.__headers_and['Cookie'] = re.sub('did=.*?;', 'did=' + did + ';', self.__cookie)
            video_url = WORK_URL + vid
            resp = requests.get(video_url, headers=self.__headers_and,  params={"did": did},timeout=20
                                # proxies=proxies
                                )
            resp.raise_for_status()
            html = resp.text

            pattern = '"srcNoMark":"(https:.*?).mp4'
            '''无水印：https://txmov2.a.yximgs.com/upic/2020/09/01/11/BMjAyMDA5MDExMTE3MThfMTM1Njk3NTc3OV8zNTM2NjQ2OTUxNF8wXzM=_b_Be53756194a8110de7e2153cfef04f7b0.mp4'''
            playUrl = re.search(pattern, html).group(1) + ".mp4"
            if not nums:
                video_info = {}
                try:
                    video_info['作者'] = re.search('<div class="auth-name">(.*?)</div>', html).group(1)
                    video_info['简介'] = re.search('<div class="caption-container">(.*?)</div>', html).group(1)
                    video_info['点赞'] = re.search('"likeCount":"(.*?)",', html).group(1)
                    video_info['评论'] = re.search('"commentCount":"(.*?)",', html).group(1)
                    video_info['链接'] = playUrl
                except:
                    pass
                global USER_ITEM
                USER_ITEM = video_info

            resp_pro = requests.get(playUrl, timeout=20)
            resp.raise_for_status()
            content = resp_pro.content
            with open(dir_name + vid + '.mp4', 'wb') as f:
                f.write(content)
        except Exception as e:
            print('无水印下载失败',e)
            try:
                # 获取视频链接
                payload = {"operationName": "SharePageQuery",
                           "variables": {"photoId": vid, "principalId": uid},
                           "query": "query SharePageQuery($principalId: String, $photoId: String) {\n  feedById(principalId: $principalId, photoId: $photoId) {\n    currentWork {\n      playUrl\n      __typename\n    }\n    __typename\n  }\n}\n"
                           }
                proxy_ = random.choice(IP_LIST)
                proxies = {'{}'.format(proxy_['type']): '{0}:{1}'.format(proxy_['ip'], proxy_['port'])}
                self.__headers_and['User-Agent'] = random.choice(UA_WEB_LIST)
                self.__headers_and['Cookie'] = re.sub('did=.*?;', 'did=' + did + ';', self.__cookie)
                resp = requests.post(DATA_URL, headers=self.__headers_and, json=payload,timeout=20,
                    # proxies = proxies
                )
                resp.raise_for_status()
                resp_json = resp.json()
                # 下载视频
                playUrl = resp_json['data']['feedById']['currentWork']['playUrl']
                resp_pro = requests.get(playUrl, timeout=20)
                resp.raise_for_status()
                content = resp_pro.content
                path1 = './data/'
                if not os.path.exists(path1):
                    os.makedirs(path1)
                with open(dir_name + vid + '.mp4', 'wb') as f:
                    f.write(content)
            except Exception as e:
                print('有水印下载失败', e)
    # 6.获取用户个人信息
    def get_user_info(self,uid,work_list,nickname):
        user_info = {}
        video_list = []
        for work in work_list:
            video_item = {}
            video_item['id'] = work['id']
            video_item['封面'] = work['thumbnailUrl']
            video_item['播放'] = work['counts']['displayView']
            video_item['点赞'] = work['counts']['displayLike']
            video_item['评论'] = work['counts']['displayComment']
            video_item['链接'] = WORK_URL + video_item['id']
            video_list.append(video_item)

        user_info['id'] = work_list[1]['user']['id']
        user_info['作者'] = work_list[1]['user']['name']
        user_info['头像'] = work_list[1]['user']['avatar']

        self.__headers_web['User-Agent'] = random.choice(UA_WEB_LIST)
        self.__headers_web['Cookie'] = re.sub('did=.*?;', 'did=' + random.choice(DID_AND_LIST) + ';', self.__cookie)
        payload = {"operationName": "sensitiveUserInfoQuery",
                   "variables": {"principalId": uid},
                   "query": "query sensitiveUserInfoQuery($principalId: String) {\n  sensitiveUserInfo(principalId: $principalId) {\n    kwaiId\n    originUserId\n    constellation\n    cityName\n    counts {\n      fan\n      follow\n      photo\n      liked\n      open\n      playback\n      private\n      __typename\n    }\n    __typename\n  }\n}\n"}
        resp = requests.post(DATA_URL, headers=self.__headers_web, json=payload,
                             # proxies=proxies
                             )
        resp_json = resp.json()
        userif = resp_json['data']['sensitiveUserInfo']
        try:
            user_info['星座'] = userif['constellation']
            user_info['城市'] = userif['cityName']
            user_info['粉丝'] = userif['counts']['fan']
            user_info['关注'] = userif['counts']['follow']
            user_info['作品'] = userif['counts']['photo']
        except:
            pass
        global USER_ITEM
        USER_ITEM = user_info
        user_info['video_list'] = video_list
        with open('./data/{}.json'.format(nickname),'w', encoding='utf8') as f:
            json.dump({'item':user_info}, f, indent=4, ensure_ascii=False)
# 自定义qt线程执行后台任务
class Runthread(QThread):
    #  通过类成员对象定义信号对象
    signal = pyqtSignal(str)
    def __init__(self,start_url,reviewEdit):
        super(Runthread, self).__init__()
        self.start_url = start_url
        self.reviewEdit = reviewEdit
    def __del__(self):
        self.wait()
    def run(self):
        try:
            self.list_flag = []
            def start_spider(signal,list_flag):
                # 进度条设置进度
                for i in range(96):
                    time.sleep(0.6)
                    if len(list_flag) == 1:
                        break
                    # 注意这里与_signal = pyqtSignal(str)中的类型相同
                    signal.emit(str(i))
            # 开启线程并启动
            t = threading.Thread(target=start_spider, args=(self.signal,self.list_flag))
            t.start()
            # 启动爬虫
            spider_KS = spider_ks(self.start_url, cookie)
            spider_KS.spider_start()
            # 模拟耗时操作
            # sleep(40)
            print('下载完成')
            self.list_flag.append(0)
            self.signal.emit(str(100))
        except Exception as e:
            print(e)
            self.reviewEdit.setText('下载出错:',e)
# 前台界面
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        # 文本输入框
        self.ipput_Edit = QLineEdit()
        self.ipput_Edit.setPlaceholderText('请输入快手用户分享链接或视频分享链接...')
        # 点击下载框
        self.download_Button = QPushButton('下载')
        # 添加槽函数
        # download_Button.clicked.connect(self.pro_show)
        self.download_Button.clicked.connect(lambda: self.buttonClicked())
        # 进度条
        self.pro_bar = QProgressBar()
        # 详情显示框
        self.reviewEdit = QTextEdit()
        # 设置布局
        grid = QGridLayout()
        grid.setSpacing(10)
        # 配置网格布局
        grid.addWidget(self.ipput_Edit, 1, 0)
        grid.addWidget(self.download_Button, 1, 1)
        grid.addWidget(self.pro_bar,2,0,1,2)
        grid.addWidget(self.reviewEdit, 3, 0,5,2)
        self.setLayout(grid)
        self.thread = None
        # 设置窗口
        self.resize(360, 250)
        self.setWindowTitle('快手无水印视频下载')
        self.show()

    # 设置进度条以及按钮改变
    def call_backlog(self, msg):
        # 将线程的参数传入进度条以及显示框
        self.pro_bar.setValue(int(msg))
        self.reviewEdit.setText(msg)
        # 达到满进度时设置下载按钮状态
        if msg == '100':
            del self.thread
            self.reviewEdit.setText('下载完成')
            self.download_Button.disconnect()
            self.download_Button.clicked.connect(QCoreApplication.quit)
            self.download_Button.setEnabled(True)
            self.download_Button.setText('完成')
            # print(USER_ITEM)
            if USER_ITEM.get('video_list') != None:
                del USER_ITEM['video_list']
            for name,value in USER_ITEM.items():
                self.reviewEdit.append(str(name) +':'+str(value))

    def buttonClicked(self):
        self.download_Button.setEnabled(False)
        # 获取用户输入链接
        input_text = ''.join(self.ipput_Edit.text().split('\n')).strip()
        start_url = input_text
        # start_url = 'https://v.kuaishouapp.com/s/fkbxgtrb '
        try:
            if 'https://v.kuaishouapp.com' not in start_url:
                raise ValueError("必须是url链接")
            # 设置按钮
            self.download_Button.setText('下载中')
            self.thread = Runthread(start_url,self.reviewEdit)
            self.thread.signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
            self.thread.start()
        except Exception as e:
            set_text = '链接不正确，请重新输入或换一个链接。{}'.format(e)
            self.reviewEdit.setText(set_text)
            self.download_Button.setEnabled(True)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    # 个人主页的分享链接
    # start_url = 'https://v.kuaishouapp.com/s/gZB2Lgx2 '
    # 单个视频
    # start_url = 'https://v.kuaishouapp.com/s/PpGiewIE '


'''
加入了UI
可自动识别主页链接或者视频链接
先下载无水印的，如果出现验证则下载有水印的
加入了随机代理和随机UA和随机did
需要cookie
我是谁
'''