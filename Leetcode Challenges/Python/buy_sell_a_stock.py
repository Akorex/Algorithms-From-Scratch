"""Solution to Leetcode problem # 121 - Best time to buy and sell stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
from typing import List

# initial approach - doesn't work for edge case eg [2, 4, 1]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices.index(min(prices))
        temp_max = 0
        
        for i in range(start, len(prices)):
            if prices[i] > temp_max:
                temp_max = prices[i]
                
        profit = temp_max - min(prices)
        return profit