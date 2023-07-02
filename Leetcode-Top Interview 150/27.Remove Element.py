# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 00:26:57 2023

@author: HP
"""

class Solution:
    def removeElement(self, nums, val):
        nums[:] = (value for value in nums if value != val)
        k = len(nums)
        return k