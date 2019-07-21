# coding=utf-8
# @Time    : 2019/5/29 17:38
# @Author  : zwa
import redis

rc = redis.StrictRedis(host='192.168.x.x', port='6379',decode_responses=True)
ps = rc.pubsub()
ps.subscribe('xxxxx')  # 从xxxxx订阅消息
for item in ps.listen():  # 监听状态：有消息发布了就拿过来
    if item['type'] == 'message':
        # print(item['channel'])  # 频道名称
        print(item['data'])
