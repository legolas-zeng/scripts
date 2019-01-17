# coding=utf-8
'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''

class Solution(object):
    def removeDuplicates(nums):
        new_nums = []
        for x in nums:
            if x not in new_nums:
                new_nums.append(x)
        print(new_nums)
        return len(new_nums)

a = Solution
print(a.removeDuplicates(nums = [1,1,2]))

