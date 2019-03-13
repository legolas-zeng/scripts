# coding=utf-8

def mulby(num):
    print(num)
    def gn(val):
        return num * val
    return gn

zw = mulby(7)
print(zw(9));