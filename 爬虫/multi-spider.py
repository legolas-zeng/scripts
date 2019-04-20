# -*-coding:utf-8 -*-
import threading
import Queue
import time
import requests,re,shutil


'''
GIL和多线程锁:
    一个进程下可以启动多个线程,多个线程共享父进程的内存空间,也就是意味着每个线程都可以同时访问一份数据
    GIL:
        GIL就是一个互斥锁,在线程中一次只允许一个线程对变量进行修改。
            GIL并不是Python的特性,而是实现Python解析器是所引入的一个语法标准。
'''

'''

    递归锁和信号量：
        递归锁就是在一把大锁中还包含子锁
    递归锁：
        lock = threading.RLock() #进行设置一个锁
            class MyThread(threading.Thread):
                def Run():
                    lock.acquire()　＃加锁
                        num+=1
                    lock.release() # 解锁
    信号量(Semaphore):
        互斥锁同时允许一个人线程进行更改数据,而Semaphore同时允许一定数量的线程更改数据
'''

'''
线程间同步和交互
    Events是一个线程之间进行数据交换的对象,一般是一个线程判断另外一个线程是否执行完毕
    event  = threading.Event()
    event.wait() #标签如果没设置就一直等待
    event.set()  设置标签
    event.isSet()  判断是否设置标签,如果设置了返回true
    event.clear() 清空设置标签
'''
'''
    队列(queu):
        在多个线程之间进行数据交换的时候使用队列
        queue.Queue(naxsuze=0) 先进先出
        queue.LifoQueue(maxsize=0) 先进后出
        queue.PriorityQueue(maxsize=0)#存储数据时可设置优先级的队列
    queue方法:
        queue.get()  阻塞的方法
        queue.get_nowait() #非阻塞，如果为空则报 queue.Empty 异常
        queue.put()  阻塞的方法
        queuq.put_nowait() #非阻塞,如果满的话就报queue.Full 异常
        queue.qsize()  拿到queue的长度
        queue.empty()  队列是否为空
        queue.full()  队列是否满了
        queue.put(item.block=True,timeout=None) #放入数据,默认是block的，当queue满的时候put就会进行阻塞,Timeout是阻塞情况下多长时间后就进行报异常
        queue.put_nowait(item)  非阻塞,满了就抛异常
        queue.get(block=True,timeout=None) #取出数据,默认是block的,当queue满的时候get会进行阻塞等待,如果超出timeout时间则报错,默认是一直阻塞中
        queue.get_nowait() #拿出数据
        queue.task_done() # 一个queue通知另外一个queue某个任务已完成。
'''

SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 5   #设置线程个数

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()
pagemun = 1000
urlbase = 'http://www.o23g.com/cn/vl_genre.php?&mode=&g=argq&page='
# urlbase = 'http://www.o23g.com/cn/vl_genre.php?&mode=&g=araa&page='

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
    image_path = 'H:\images'
    # image_path = 'G:\\rukong'
    temp = image_path + '/%s.jpg' % x
    print('正在下载图片%s' % x)
    imgurl = 'http:' + url
    print(imgurl)
    r = requests.get(imgurl, stream=True)
    if r.status_code == 200:
        with open(temp, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def worker():
    global SHARE_Q              # 线程通信的方式————共享变量
    while not SHARE_Q.empty():
        info = SHARE_Q.get()  # 获得任务，是一种阻塞的方法，线程安全的操作
        downloadimage(info[0],info[1],info[2])
        # time.sleep(1)
        SHARE_Q.task_done()


def main():
    global SHARE_Q
    threads = []
    for a in range(998, pagemun):
        i = a + 1
        print('--------------正在下载第%s页的图片---------------' % i)
        url = urlbase + str(i)
        info = filterpage(url)
        for data in info:
            x = data[0]
            imgurl = data[1][:-5] + 'l.jpg'
            info=[i,x,imgurl]
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
    print("图片全部爬取完了")

if __name__ == '__main__':
    main()