# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:26:26 2023

@author: HP
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # i = 0
        # mul = 1
        #output = []
        # while i < len(nums):
        #     for j in range(len(nums)):
        #         if i != j:
        #             mul = mul*nums[j]
        #     output.append(mul)
        #     mul = 1
        #     i = i + 1
        # return output
        mul = 1
        output = list(range(len(nums)))
        for num in nums:
            mul = mul*num
        if mul != 0:
            for i in range(len(nums)):
                output[i] = mul/nums[i]
        else:
            i = 0
            mul = 1
            output = []
            while i < len(nums):
                for j in range(len(nums)):
                    if i != j:
                        mul = mul*nums[j]
                output.append(mul)
                mul = 1
                i = i + 1
        return output