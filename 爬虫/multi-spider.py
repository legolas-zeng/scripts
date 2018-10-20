# -*-coding:utf-8 -*-
import threading
import Queue
import time
import requests,re,shutil

SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 5   #设置线程个数

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()
pagemun = 186
# urlbase = 'http://www.o23g.com/cn/vl_genre.php?&mode=&g=argq&page='
urlbase = 'http://www.o23g.com/cn/vl_genre.php?&mode=&g=araa&page='

def getPage(url):
    r=requests.get(url)
    response = r.text
    return response

def filterpage(url):
    pageCode = getPage(url)
    pattern = re.compile('<div class="id">(.*?)</div><img src=\"(.*?)\" width=',re.S)
    items = re.findall(pattern, pageCode)
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(), item[1].strip()])
    return pageStories
def downloadimage(i,x,url):
    # image_path = 'C:\Users\Administrator\Desktop\\newimages'
    image_path = 'G:\\rukong'
    temp = image_path + '/%s.jpg' % x
    print u'正在下载图片%s' % x
    imgurl = 'http:' + url
    print imgurl
    r = requests.get(imgurl, stream=True)
    if r.status_code == 200:
        with open(temp, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        info = SHARE_Q.get()  # 获得任务
        downloadimage(info[0],info[1],info[2])
        # time.sleep(1)
        SHARE_Q.task_done()


def main():
    global SHARE_Q
    threads = []
    for a in range(83, pagemun):
        i = a + 1
        print u'--------------正在下载第%s页的图片---------------' % i
        url = urlbase + str(i)
        info = filterpage(url)
        for data in info:
            x = data[0]
            imgurl = data[1][:-5] + 'l.jpg'
            info=[i,x,imgurl]
            SHARE_Q.put(info)
        print u"任务队列加载完成"
        for i in xrange(_WORKER_THREAD_NUM): #开始线程，从0到2
            print u"开始处理第%s个线程"%i
            thread = MyThread(worker)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    SHARE_Q.join()
    print u"图片全部爬取完了"

if __name__ == '__main__':
    main()