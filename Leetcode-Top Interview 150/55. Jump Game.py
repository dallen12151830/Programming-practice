# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:11:03 2023

@author: HP
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        test = True
        for i in nums:
            if i == 0:
                test = False
                break
        if test == True:
            return True
            
        last_index = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= last_index:
                last_index = i
        return last_index == 0