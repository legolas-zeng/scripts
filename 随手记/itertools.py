# coding=utf-8
import itertools
def get_letter(i):
    return chr(ord('a')+i)
r = range(10)
print(list(map(get_letter, r)))

print(list((get_letter(i) for i in range(10))))

print(chr(ord('a'+i)) for i in range(10))

sum(range(20, 30))

# 连接多个列表或者迭代器
x = itertools.chain(range(3), range(4), [3,2,1])
print(list(x))

# 累加
x = itertools.accumulate(range(10))
print(list(x))

# 简单的生成一个拥有指定数目元素的迭代器
x = itertools.repeat(0, 5)
print(list(x))
