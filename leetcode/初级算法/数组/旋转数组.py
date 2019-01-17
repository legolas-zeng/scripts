# coding=utf-8

'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

nums = [1,2,3,4,5,6,7]
new_nums = []
print(nums[-3])
k = 1
for i in range(0,len(nums)):
    new_nums.append(nums[-k+i])
print(new_nums)