# -*-coding:utf-8 -*-

# 阶乘
def test(x):
    if x<=1:
        return x
    return x*test(x-1)
print test(3)

a = lambda x: x  if x<=1 else x*a(x-1)
print a(3)

