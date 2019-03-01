# coding=utf-8
from multiprocessing import Pool
import os, time, redis,multiprocessing,requests,hashlib,json,math
import pandas as pd
from dateutil.parser import parse


def Writecsv(imei):
    head = ["head1"]
    l = [imei]
    df = pd.DataFrame(l, columns=head)
    df.to_csv("D:\entropy2.csv", encoding="utf-8")

def GetRedisdata(imei,i):
    print(imei,i)
    return imei

if __name__=='__main__':
    start = time.time()
    df = pd.read_excel(r'D:\imei.xlsx')
    p = Pool(multiprocessing.cpu_count())
    st = '2018-05-25' + ' 07:00:00'
    for i in range(len(df)):
        p.apply_async(GetRedisdata,args=(str(df['imei'][i]),i),callback=Writecsv)
    print('等待所有子进程完成...')
    p.close()  # 关闭进程池,不在接收新的任务
    p.join()
    print('所有子进程完成.')
    end = time.time()
    print('所有任务完成共使用 %0.2f seconds.' % (end - start))