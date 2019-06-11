# coding=utf-8
# @Time    : 2019/4/23 15:04
# @Author  : zwa

'''
用两个列表来组成字典
'''
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))

'''
zip(iterable)从iterable中依次取一个元组，组成一个元组。
Zip() 内置函数使用多个可迭代对象作为输入并返回元组列表。每个元组列表依据位置索引对输入对象的元素进行分组。
用户也可以使用 *zip()  来解压对象
'''
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
print(list(tuple1))

'''
*zip()函数是zip()函数的逆过程，将zip对象变成原先组合前的数据。
'''
print(*zip(tuple1))

## zip()应用
# 矩阵相加减、点乘
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
# 矩阵点乘
print('=*'*10 + "矩阵点乘" + '=*'*10)
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
# 矩阵相加,相减雷同
print('=*'*10 + "矩阵相加,相减" + '=*'*10)
print([x+y for a, b in zip(m, n) for x, y in zip(a, b)])