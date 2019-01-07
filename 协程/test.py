# coding=utf-8
import requests
import time,asyncio

async def test2(i):
    r = await other_test(i)
    print(i,r)

async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(4)
    print(time.time()-start)
    return r

url = ["https://segmentfault.com",
       "https://www.jianshu.com",
       "https://www.baidu.com/"]

loop = asyncio.get_event_loop() # 创建一个循环
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task))  # 检测task运行情况并返回结果
endtime = time.time()-start
print(endtime)
loop.close()