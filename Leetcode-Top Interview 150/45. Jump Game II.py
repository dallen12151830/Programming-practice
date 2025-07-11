# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:40:36 2023

@author: HP
"""

class Solution:
    def jump(self, nums):
        x = [nums[i]+ i for i in range(len(nums))]

        l, r, jump = 0, 0, 0
        while r < len(nums)-1:
            jump += 1
            l, r = r+1, max(x[l: r+1])
        return jump