# -*-coding:utf-8 -*-
a = '1123456789'
print(a[1:2])
print(a[:-5])
l = len(a)
prefix = a[0:l%3]
li = []
for i in range(l/3,0,-1):
    if i == 1:
        b = -3
        c = None
    else:
        b = -3 * i
        c = int(b)+3
    str1 = ','+a[b:c]
    li.append(str1)
str2 = "".join(li)
print(prefix+str2)

