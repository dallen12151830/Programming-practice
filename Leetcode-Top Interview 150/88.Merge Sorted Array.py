# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 00:41:25 2023

@author: HP
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            nums1[-n:] = nums2
            nums1.sort()
        else:
            pass
