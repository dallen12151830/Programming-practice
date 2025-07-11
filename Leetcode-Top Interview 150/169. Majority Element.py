# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:33:19 2023

@author: HP
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        len_nums = len(nums)
        if len_nums%2 == 0:
            return nums[len_nums/2]
        else:
            return nums[(len_nums+1)/2-1]