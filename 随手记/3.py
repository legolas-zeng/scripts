# -*-coding:utf-8 -*-
def comma(s):
    n = len(s)
    if n <=3:
        return s
    return comma(s[:n-3])

# print comma('1245')

def sum(s):
    a = int(s)
    a = a-1
    if a<=0:
        return a
    return sum(a)+a
print(sum('12'))