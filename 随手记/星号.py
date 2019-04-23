# coding=utf-8
# @Time    : 2019/4/22 14:16
# @Author  : zwa


def d(a, b, c):
    print(a, b, c)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]

'''
解释器将自动将a进行解包成1,2,3,然后传递给多个单变量参数（参数个数要对应相等）
'''
d(*a)

'''
*parameter是用来接受任意多个参数并将其放在一个元组中。
'''
def d4(*args):
    print(args)
d4(*b)

dictionary = {"a": 1, "b": 2}
def someFunction(a, b):
   return (a + b)

print(someFunction(**dictionary))

