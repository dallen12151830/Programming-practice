# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:46:57 2023

@author: HP
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a = [0] * len(nums)
        a = {}
        b = nums[0]
        for i in nums:
            if i == b:
                sum = sum+1
            else:
                c = i
        if sum > len(nums)/2:
                return sum
        else:
                return c

