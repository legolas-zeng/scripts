# coding=utf-8
# @Time    : 2019/4/22 17:17
# @Author  : zwa

'''
map() 对X中的每个元素应用了简单的lambda函数
它返回一个map object类型，可以被转换成一些可迭代对象，例如列表或元组
'''
x = [1, 2, 3]
y = map(lambda x : x + 1 , x)
print(list(y))

'''
str转int
'''
l=map(int,'1234')
for i in l:
    print(type(i))
    print(i)

'''
将小写转成大写
'''
def u_to_l (s):
    return s.upper()
print(map(u_to_l,'asdfd'))


'''
map()函数将一个全部为int的列表，转化为全部为str的列表
'''
print(list(map(str,[1,2,3,4,5,6,7,8])))

'''
map()函数将一个全部为str的列表，转化为全部为int的列表
'''

print(list(map(int,['1','2','23','8'])))


class someClass:
   def __repr__(self):
       return "字符串表示对象的“官方”方法很实用"
someInstance = someClass()
print(someInstance)

'''
这种情况是因为在python3里面，map()的返回值已经不再是list,而是iterators, 所以想要使用，只用将iterator 转换成list 即可,比如list(map())
提取字典的key，并将结果存放在一个list中
'''
print(map(int, {1:2,2:3,3:4}))
print(list(map(int,{1:2,2:3,3:4})))
