# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:44:48 2023

@author: HP
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if len(nums) >= k:
        #     nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]

        # else:
            # nums[:] = nums[len(nums)-(k%len(nums)):]+nums[:len(nums)-(k%len(nums))]
        nums[:] = nums[len(nums)-(k%len(nums)):]+nums[:len(nums)-(k%len(nums))]
