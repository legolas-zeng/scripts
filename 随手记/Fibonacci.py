# coding=utf-8
def fab(max):
   n, a, b = 0, 0, 1
   L = []
   while n < max:
       L.append(b)
       a, b = b, a + b
       n = n + 1
   return L

# 容器是用来储存元素的一种数据结构，容器将所有数据保存在内存中，Python中典型的容器有：list，set，dict，str等等。
class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    '''
    可迭代器
    '''
    def __iter__(self):
        return self
# 2.7版本是next(self),3.7版本的是__next__(self)
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

'''
for … in… 这个语句其实做了两件事。第一件事是获得一个可迭代器，即调用了__iter__()函数。 
第二件事是循环的过程，循环调用next()函数。
'''
# for n in Fab(5):
#     print(n)

'''
yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，
调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
'''
def fab2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

for n in fab2(5):
    print(n)

