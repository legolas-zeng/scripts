# coding=utf-8
# @Time    : 2019/6/10 15:16
# @Author  : zwa

import ReFlect.Tests
module = __import__('Tests')
f = getattr(module,'Printmethod')
f()



if hasattr(module,"printtxts"):
    module.printtxt()
else:
    print('方法不存在')