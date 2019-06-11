# coding=utf-8
# @Time    : 2019/6/5 10:42
# @Author  : zwa

'''
其实，反射就是通过字符串的形式，导入模块；通过字符串的形式，去模块寻找指定函数，并执行。利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！

我们常常会遇到这样的需求：需要执行对象里的某个方法，或需要调用对象中的某个变量，但是由于种种原因我们无法确定这个方法或变量是否存在，
这是我们需要用一个特殊的方法或机制要访问和操作这个未知的方法或变量，这中机制就称之为反射。
'''

# 判断对象中是否有这个方法或变量
'''
class Person(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("%s正在交谈"%self.name)

p = Person("laowang")
print(hasattr(p,"talk"))    # True。因为存在talk方法
print(hasattr(p,"name"))    # True。因为存在name变量
print(hasattr(p,"abc"))     # False。因为不存在abc方法或变量

'''


# 获取对象中的方法或变量的内存地址
'''
class Person(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("%s正在交谈"%self.name)
p = Person("laowang")

n = getattr(p,"name")   # 获取name变量的内存地址
print(n)                # 此时打印的是:laowang

f = getattr(p,"talk")   # 获取talk方法的内存地址
f()                     # 调用talk方法

# 我们发现getattr有三个参数，那么第三个参数是做什么用的呢?
s = getattr(p,"abc","not find")
print(s)                # 打印结果：not find。因为abc在对象p中找不到，本应该报错，属性找不到，但因为修改了找不到就输出not find
'''

# 为对象添加变量或方法

'''
def abc(self):
    print("%s正在交谈"%self.name)

class Person(object):
    def __init__(self,name):
        self.name = name

p = Person("laowang")
setattr(p,"talk",abc)   # 将abc函数添加到对象中p中，并命名为talk
p.talk(p)               # 调用talk方法，因为这是额外添加的方法，需手动传入对象


setattr(p,"age",30)     # 添加一个变量age,复制为30
print(p.age)            # 打印结果:30
'''

# 删除对象中的变量。注意：不能用于删除方法
'''
class Person(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("%s正在交谈"%self.name)

p = Person("laowang")

delattr(p,"name")       # 删除name变量
print(p.name)           # 此时将报错
'''
# callable方法，如果传入的参数是可以调用的函数，则返回true，否则返回false。

import re

print(callable(getattr(re,'split'))) # 输出True

print(callable(getattr(re,'__doc__'))) # 输出False
