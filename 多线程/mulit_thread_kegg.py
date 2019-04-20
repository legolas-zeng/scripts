# -*- coding:utf-8 -*-
import threading
from queue import Queue
from time import sleep
import random
#下面是利用線程和queue隊列的實現方法
#繼承一個Thread類，在run方法中進行需要重複的單個函數操作
class Test(threading.Thread):
    def __init__(self,queue,lock,num):
        #傳遞一個隊列queue和線程鎖，並行數
        threading.Thread.__init__(self)
        self.queue=queue
        self.lock=lock
        self.num=num
    def run(self):
        #while True:#不使用threading.Semaphore，直接開始所有線程，程序執行完畢線程都還不死，最後的print threading.enumerate()可以看出
        with self.num:#同時並行指定的線程數量，執行完畢一個則死掉一個線程
            #以下為需要重複的單次函數操作
            n=self.queue.get()#等待隊列進入
            lock.acquire()#鎖住線程，防止同時輸出造成混亂
            print('開始一個線程：',self.name,'模擬的執行時間：',n)
            print('隊列剩餘：',queue.qsize())
            print(threading.enumerate())
            lock.release()
            sleep(n)#執行單次操作，這裡sleep模擬執行過程
            self.queue.task_done()#發出此隊列完成信號
threads=[]
queue=Queue()
lock=threading.Lock()
num=threading.Semaphore(3)#設置同時執行的線程數為3，其他等待執行
#啟動所有線程
for i in range(10):#總共需要執行的次數
    t=Test(queue,lock,num)
    t.start()
    threads.append(t)
    #吧隊列傳入線程，是run結束等待開始執行，放下面單獨一個for也行，這裡少個循環吧
    n=random.randint(1,10)
    queue.put(n)#模擬執行函數的逐個不同輸入
#吧隊列傳入線程，是run結束等待開始執行
#for t in threads:
#    n=random.randint(1,10)
#    queue.put(n)
#等待線程執行完畢
for t in threads:
    t.join()
queue.join()#等待隊列執行完畢才繼續執行，否則下面語句會在線程未接受就開始執行
print('所有執行完畢')
print(threading.active_count())
print(threading.enumerate())