# coding=utf-8
# @Time    : 2019/12/24 17:43
# @Author  : zwa
# @Motto   ：❤lqp 

import threading
import queue
import time
import requests,re,shutil


SHARE_Q = queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 5   #设置线程个数
headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()

pagemun = 10
urlbase = 'https://movie.douban.com/top250?start='

def getPage(url):
    r=requests.get(url,headers=headers)
    response = r.text
    return response

def filterpage(url):
    pageCode = getPage(url)
    pattern = re.compile('<img width="100" alt="(.*?)" src="(.*?)" class="">',re.S)
    items = re.findall(pattern, pageCode)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(), item[1].strip()])
    return pageStories

def downloadimage(imagename,imgurl):
    image_path = 'C:\\Users\\Administrator.000\Desktop\images'
    # for i in range(25):
    temp = image_path + '/%s.jpg' % imagename
    print('正在下载图片%s' % imagename)
    r = requests.get(imgurl, stream=True)
    if r.status_code == 200:
        with open(temp, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def worker():
    global SHARE_Q              # 线程通信的方式————共享变量
    while not SHARE_Q.empty():
        info = SHARE_Q.get()  # 获得任务，是一种阻塞的方法，线程安全的操作
        downloadimage(info[0],info[1])
        # time.sleep(1)
        SHARE_Q.task_done()


def main():
    global SHARE_Q
    threads = []
    for a in range(0, pagemun):
        num = a * 25
        i = a + 1
        print('--------------正在下载第%s页的图片---------------' % i)
        url = urlbase + str(num) + '&filter='
        pageStories = filterpage(url)
        for j in range(25):
            imagename = pageStories[j][0]
            imgurl = pageStories[j][1]
            info=[imagename,imgurl]
            SHARE_Q.put(info)  # 往队列放数据，如果队列满了，这个方法会被阻塞
        print("任务队列加载完成")
        for i in range(_WORKER_THREAD_NUM): #开始线程，从0到2
            print("开始处理第%s个线程"%i)
            thread = MyThread(worker)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    SHARE_Q.join()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('总共用时：', end_time - start_time)