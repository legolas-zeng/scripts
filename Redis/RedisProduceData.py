# coding=utf-8
# @Time    : 2019/5/29 16:15
# @Author  : zwa
import redis,time
from threading import Thread

class RedisCach(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = '6379'
        self.r = redis.StrictRedis(host=self.host, port=self.port,decode_responses=True)
    def insertRedis(self, keyName, jsonStr):
        self.r.publish(keyName, jsonStr) #发布消息

'''
发布消息到“rrjc_msg”频道
在redis客户端执行"SUBSCRIBE rrjc_msg"就可以看到订阅的数据
'''
def publisher():
    r = RedisCach()
    a = 1
    while True:
        r.insertRedis("legolas",str(a))
        a += 1
        time.sleep(2)

if __name__ == "__main__":
    Thread(target=publisher).start()
