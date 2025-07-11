# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:42:23 2023

@author: HP
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minbuy = prices[0]
        sum = 0
        for i in range(len(prices)):
            minbuy = min(minbuy, prices[i])
            profit = max(prices[i]-minbuy, profit)
            
            if profit > (prices[i]-minbuy):
                sum = sum + profit
                minbuy = prices[i]
                profit = 0
        sum = sum + profit
        return sum
        