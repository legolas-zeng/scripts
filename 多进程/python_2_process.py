# coding=utf-8
# @Author  : zwa
'''
测试一下python2版本的多进程是否有什么不一样。
'''
from multiprocessing import Pool
import time

def tests(i):
    time.sleep(2)
    print(i)

if __name__ == "__main__":
    start = time.time()
    p = Pool(4)
    for data in range(100):
        print(data)
        p.apply_async(tests, args=(data,))
    print('等待所有子进程完成...')
    p.close()
    p.join()
    print('所有子进程完成.')
    end = time.time()
    print('所有任务完成共使用 %0.2f seconds.' % (end - start))