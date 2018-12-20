# coding=utf-8

class A (object):
    def __init__(self):
        self.one = '1'
        self.two = '2'
    def output(self,*args):
        print args
        print self.one
        print self.two
    def fanhui(self):
        return '321'

# B = A()
# B.output("123")

class C (A):
    def __init__(self):
        self.three = '3'
        # A.__init__(self)
        # super(C, self).__init__()
    def shuchu(self):
        data = A.fanhui(self)
        print data

D = C()
D.shuchu()
D.output()