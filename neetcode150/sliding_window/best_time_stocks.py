from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        # l maintains the lowest buying point we've found
        # r represents the current selling point
        l, r, res = 0, 1, 0
        while r < len(prices):
            res = max(prices[r] - prices[l], res)
            if prices[r] <= prices[l]:
                l = r
            r += 1

        return res