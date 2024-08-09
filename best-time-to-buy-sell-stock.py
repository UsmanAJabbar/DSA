from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        ----------
        MAX PROFIT
        ----------
        Description:
            You are given an array prices where `prices[i]` is the price of a given stock on the `i`th day.

            You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
            
            Returns the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

            Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
        """
        max_profit = 0
        l, r = 0, 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r

            r += 1

        return max_profit
