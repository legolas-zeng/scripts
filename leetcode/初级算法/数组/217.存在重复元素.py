# coding=utf-8
'''
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
'''
nums = [1,2,3,1]

'''
经过测试，list会超时,时间复杂度O(n^2),空间复杂度O(1)
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        z = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    z +=1
                    return True
                    exit(0)
        if z == 0:
            return False

'''
d = list() 用时13856 ms ,d = set() 用时40 ms
'''

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 0 or len(nums) == 1:
        return False
    # d = list()
    d = set()
    for i in nums:
        if i in d:
            return True
        d.add(i)
        print(d)
    return False

"""
set()是一个无序不重复元素集,如果存在重复元素,集合长度会改变，用于关系测试和消除重复元素。
return len(set(nums))!=len(nums)
"""

print(len(set(nums))!=len(nums))
print(set(nums),len(set(nums)),len(nums))




