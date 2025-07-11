# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:43:27 2023

@author: HP
"""

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0: return 0
        else:
            profit = 0
            minBuy = prices[0]
            for i in range(len(prices)):
                profit = max(prices[i] - minBuy, profit)
                minBuy = min(minBuy, prices[i])
            return profit
