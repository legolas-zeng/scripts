# coding=utf-8
# @Time    : 2019/6/10 14:57
# @Author  : zwa
import re

def printtxt():
    print('1111111')

def Printmethod():
    print(callable(getattr(re,'split')))
    print(callable(getattr(re,'__doc__')))
#
# # 下面这段代码列出对象所有函数：
# methodList = [method for method in dir(re) if callable(getattr(re,method))]
#
# print(methodList)
#
# print(globals())
