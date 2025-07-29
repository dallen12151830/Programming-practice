# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:46:57 2023

@author: HP
"""

class Solution(object):
    def majorityElement(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums[:] = nums[-k%len(nums):] + nums[:len(nums)-k]
        print(nums[:len(nums)-k])
        print(nums[-k:])
        print(4%5)
        return nums[:]
sol = Solution()
print(sol.majorityElement([1, 2], -7))