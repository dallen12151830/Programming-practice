# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:11:17 2023

@author: HP
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse= True)
        h_index = 0
        for i in range(len(citations)):
            if citations[i] > i:
                h_index = i+1
            else:
                break
        return h_index