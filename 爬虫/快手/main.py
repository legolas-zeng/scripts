# coding=utf-8

import requests,os
import json
import time


class Kuaishou:

    def __init__(self, cookie, user_id=None, time_min=None, time_max=None):
        self.cookie = cookie
        self.user_id = user_id
        self.time_min = time_min
        self.time_max = time_max
        self.videos = []
        self.downloaded = 0
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Content-Type': 'application/json',
            'Origin': 'https://live.kuaishou.com',
            'Host': 'live.kuaishou.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Referer': 'https://live.kuaishou.com/profile/%s' % self.user_id,
            'Cookie': self.cookie
        }

    def download(self, url, fileName=None, folder=None):
        if (not fileName) or fileName.find('{default}') > -1:
            end = url.find('?')
            if end > -1:
                default = url[url.rfind('/'):end]
            else:
                default = url[url.rfind('/'):]
            if fileName:
                fileName = fileName.replace('{default}', default)
            else:
                fileName = default

        if not folder:
            folder = 'download'

        path = r'%s/%s' % (folder, fileName)
        if not os.path.exists(path):
            if not os.path.exists(folder):
                os.makedirs(folder)

            with open(path, "wb") as file:
                response = requests.get(url, stream=True, timeout=120)
                for data in response.iter_content(chunk_size=1024 * 1024):
                    file.write(data)
                    self.downloaded += len(data)
                response.close()
            time.sleep(2)
        else:
            time.sleep(5)

    def getUrl(self, user_id, video_id):
        url = "https://live.kuaishou.com/m_graphql"
        param = '{"operationName":"SharePageQuery","variables":{"photoId":"%s",\
        "principalId":"%s"},"query":"query SharePageQuery($principalId: String, $photoId: String)\
         {\\n  feedById(principalId: $principalId, photoId: $photoId) {\\n    currentWork {\\n      playUrl\\n\
         __typename\\n    }\\n    __typename\\n  }\\n}\\n"}' % (video_id, user_id)
        data = requests.post(url, timeout=30, headers=self.headers, data=param)
        data = data.json()['data']
        '''
        此处容易报错，应该是对请求的频率有限制
        '''
        url = data['feedById']['currentWork']['playUrl']
        return url

    def getVideos(self):
        url = "https://live.kuaishou.com/m_graphql"
        param = "{\"operationName\":\"privateFeedsQuery\",\"variables\":{\"principalId\":\"%s\",\
            \"pcursor\":\"\",\"count\":24},\"query\":\"query privateFeedsQuery($principalId: String, \
            $pcursor: String, $count: Int) {\\n  privateFeeds(principalId: $principalId, pcursor: $pcursor,\
            count: $count) {\\n    pcursor\\n    list {\\n      id\\n      thumbnailUrl\\n      poster\\n\
            workType\\n      type\\n      useVideoPlayer\\n      imgUrls\\n      imgSizes\\n      magicFace\\n\
            musicName\\n      caption\\n      location\\n      liked\\n      onlyFollowerCanComment\\n\
            relativeHeight\\n      timestamp\\n      width\\n      height\\n      counts {\\n        displayView\\n\
            displayLike\\n        displayComment\\n        __typename\\n      }\\n\
            user {\\n        id\\n        eid\\n        name\\n        avatar\\n        __typename\\n      }\\n\
            expTag\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}" % self.user_id
        data = requests.post(url, timeout=10, headers=self.headers, data=param)
        # print(data.text)
        data = data.json()['data']['privateFeeds']
        pcursor = data['pcursor']
        is2Break = False
        time_min = None
        time_max = None
        if self.time_min:
            time_min = time.mktime(time.strptime(self.time_min, "%Y-%m-%d")) * 1000
        if self.time_max:
            time_max = time.mktime(time.strptime(self.time_max, "%Y-%m-%d")) * 1000
        for obj in data['list']:
            if not obj['id']:
                continue
            video = {
                'user_id': self.user_id,
                'user_name': obj['user']['name'],
                'video_id': obj['id'],
                'workType': obj['workType'],
                'caption': obj['caption'],
                'timestamp': obj['timestamp'],
            }
            if (time_min and video['timestamp'] < time_min):
                is2Break = True
                break
            if (time_max == None or video['timestamp'] < time_max + 1000 * 60 * 60 * 24):
                if video['workType'] == 'video':
                    self.videos.append(video)

        while (not is2Break) and pcursor and pcursor != 'no_more':
            if pcursor == "":
                print('cookie 失效')
                return
            param = "{\"operationName\":\"publicFeedsQuery\",\"variables\":{\"principalId\":\"%s\",\
            \"pcursor\":\"%s\",\"count\":24},\"query\":\"query publicFeedsQuery($principalId: String,\
            $pcursor: String, $count: Int) {\\n  publicFeeds(principalId: $principalId, pcursor: $pcursor, count: $count)\
             {\\n    pcursor\\n    live {\\n      user {\\n        id\\n        avatar\\n        name\\n        __typename\\n\
             }\\n      watchingCount\\n      poster\\n      coverUrl\\n      caption\\n      id\\n      playUrls {\\n\
             quality\\n        url\\n        __typename\\n      }\\n      quality\\n      gameInfo {\\n        category\\n\
             name\\n        pubgSurvival\\n        type\\n        kingHero\\n        __typename\\n      }\\n      hasRedPack\\n\
             liveGuess\\n      expTag\\n      __typename\\n    }\\n    list {\\n      id\\n      thumbnailUrl\\n      poster\\n\
             workType\\n      type\\n      useVideoPlayer\\n      imgUrls\\n      imgSizes\\n      magicFace\\n      musicName\\n\
             caption\\n      location\\n      liked\\n      onlyFollowerCanComment\\n      relativeHeight\\n      timestamp\\n\
             width\\n      height\\n      counts {\\n        displayView\\n        displayLike\\n        displayComment\\n\
             __typename\\n      }\\n      user {\\n        id\\n        eid\\n        name\\n        avatar\\n        __typename\\n\
             }\\n      expTag\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}" % (self.user_id, pcursor)
            data = requests.post(url, timeout=10, headers=self.headers, data=param).json()['data']['publicFeeds']
            pcursor = data['pcursor']
            is2Break = False
            for obj in data['list']:
                video = {
                    'user_id': self.user_id,
                    'user_name': obj['user']['name'],
                    'video_id': obj['id'],
                    'workType': obj['workType'],
                    'caption': obj['caption'],
                    'timestamp': obj['timestamp'],
                }
                if (time_min and video['timestamp'] < time_min):
                    is2Break = True
                    break
                if (time_max == None or video['timestamp'] < time_max + 1000 * 60 * 60 * 24):
                    if video['workType'] == 'video':
                        self.videos.append(video)

        return self.videos

    def refreshCookie(self):
        '''
        // TODO
        '''
        url = "https://id.kuaishou.com/pass/kuaishou/login/passToken"
        headers = {
            'Host': 'id.kuaishou.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://live.kuaishou.com',
            'Referer': 'https://live.kuaishou.com/cate/my-follow/living',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Cookie': self.cookie
        }
        params = 'sid=kuaishou.live.web'
        data = requests.post(url, timeout=10, headers=headers, data=params).text
        print(data)

if __name__ == '__main__':
    # 读取配置
    with open(r'config.json', "r") as file:
        content = file.read()
        print(content)
        config = json.loads(content)

    for task in config['tasks']:
        # 获取时间
        if 'time_min' in task:
            time_min = task['time_min']
        elif 'time_min' in config:
            time_min = config['time_min']
        else:
            time_min = None

        if 'time_max' in task:
            time_max = task['time_max']
        elif 'time_max' in config:
            time_max = config['time_max']
        else:
            time_max = None
        # 获取任务id
        if 'user_id' in task:
            user_id = task['user_id']
        else:
            user_id = task

        print(time_max)
        downloader = Kuaishou(
            cookie=config['cookie'],
            user_id=user_id,
            time_min=time_min,
            time_max=time_max,
        )
        videos = downloader.getVideos()
        for index, video in enumerate(videos):
            print(video['video_id'])

        print('正在下载 id为 %s的视频，共有%d 个' % (user_id, len(videos)))
        for index, video in enumerate(videos):
            # 下载文件夹
            folder = config['saveFolder'] \
                .replace('{user_name}', video['user_name']) \
                .replace('{user_id}', video['user_id']) \
                .replace('{caption}', video['caption'])
            # 下载文件名
            fileName = None
            if 'fileName' in config:
                fileName = config['fileName'] \
                    .replace('{user_name}', video['user_name']) \
                    .replace('{user_id}', video['user_id']) \
                    .replace('{video_id}', video['video_id']) \
                    .replace('{caption}', video['caption'])

            print('下载进度： %d/%d' % (index + 1, len(videos)))
            dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(video['timestamp'] / 1000.0))
            print('发布日期： %s' % dtime)
            url = downloader.getUrl(video['user_id'], video['video_id'])
            print('下载链接： %s' % url)
            print('保存路径： %s%s' % (folder,fileName))
            downloader.download(url, folder=folder, fileName=fileName)
            print('%s 下载完毕' % video['caption'])