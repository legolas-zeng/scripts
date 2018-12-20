# coding=utf-8

# __all__ = ['close']
def open(file,flags,mode):
    print('123456')

def close(file,flags,mode):
    print('abcdef')

# 多个返回值
def MultReturn():
    a = 'A'
    b = 'B'
    return a,b
a = MultReturn() # 取到的是tupe
print a

# 可变参数
def VaryArg(*args):
    print args
VaryArg('1','2')

# 关键字参数
def KeyArg(**kwargs):
    print kwargs
KeyArg(a='1',b='2',c='3')


# 不定参合关键字参数
def MixArg(*args,**kwargs):
    print args
    print kwargs
MixArg('1',d='4')


