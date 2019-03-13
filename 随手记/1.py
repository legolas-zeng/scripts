# -*-coding:utf-8 -*-
c = lambda s: s if len(s)<=3 else c(s[:len(s)-3])+','+s[len(s)-3:]
print(c('12345151616156'))

def comma(s):
    n = len(s)
    if n <=3:
        return s
    return comma(s[:n-3])+','+s[n-3:]

print(comma('12345151616156'))


def point(s):
    a,b = s.split('.')
    return comma(a)+'.'+comma(b)

print(point('1234515.1616156'))
s = '1234515.1616156'

print(comma(s.split('.')[0])+'.'+comma(s.split('.')[1]))






