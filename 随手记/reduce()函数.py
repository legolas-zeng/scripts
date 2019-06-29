# coding=utf-8
# @Time    : 2019/6/14 14:45
# @Author  : zwa

'''
reduce()函数的功能是对可迭代对象（iterable）中的元素从左到右进行累计运算，最终得到一个数值。第三个参数initializer是初始数值，
可以空置，空置为None时就从可迭代对象（iterable）的第二个元素开始，并将第一个元素作为之前的结果。
'''


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

'''
lambda 参数1，参数2: 表达式
'''
plus = lambda x, y : x + y

print(reduce(plus, [1,2,3,4,5]))

print(reduce(plus, [1,2,3,4,5], 10))