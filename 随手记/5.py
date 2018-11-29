# coding=utf-8
a = [1,2,3,4]

print dir(a)
for index,name in enumerate(a):
    print index,'-',name


for item in a:
    print item

for i in range(len(a)): #直接迭代序列元素比迭代元素索引要快。
    print a[i]