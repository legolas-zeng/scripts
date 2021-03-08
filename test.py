# coding=utf-8
# @author: zwa❤lqp
# @time: 2021/2/27 17:47

import os,re

# a = 0
# b = 1
# n = 10
#
# for i in range(n):
#     a,b = b,a+b
#     print(a)


# def fib_yield_while(max):
#     a, b = 0, 1
#     while max > 0:
#         a, b = b, a + b
#     max -= 1
#     yield a
#
#
# def fib_yield_for(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
#
# for i in fib_yield_for(10):
#     print(i, end=' ')

a = ['A', '', 'B', None, 'C', ' ']
# filter()函数把传入的函数一次作用于每个元素，然后根据返回值是True 还是 False决定保留还是丢弃该元素
print(list(filter(lambda s : s and s.strip(), a)))

s = lambda x:"yes" if x==1 else "no"
print(s(1))


foo=[-5,8,0,4,9,-4,-20,-2,8,2,-4]
# 正数从小到大,负数从大到小

a = sum(range(1,101))
print(sum(range(1,101)))

b =[1,2,3,4,5]

def fn(x):
    return x**2

print(list(map(fn,b)))

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
print([i for i in [1,2,3,4,5] if i >3])


fn1 = lambda **kwargs:kwargs
print(fn1(name='lily',age=18))

print(lambda a=1,b=2:a if a > b else b)
