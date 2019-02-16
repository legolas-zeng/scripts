# coding=utf-8
# @author: zenganiu
# @time: 2019/2/16 15:40

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

'''
digits = [1,2,3]
if len(digits) == 0:
    digits = [1]
elif digits[-1] != 9 :
    digits[-1] += 1
elif digits[-1] == 9:
    digits[-1] = 0

print(digits[:-1])
