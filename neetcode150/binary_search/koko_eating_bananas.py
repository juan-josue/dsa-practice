from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We will need at least 1 banana per hr, and at most max(piles) per hr
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2

            # Determine how long it takes to eat all piles at rate k.
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i] / k)
            
            # If it can be completed at rate k within h hours, try values < k 
            if hours <= h:
                res = min(res, k)
                r = k - 1
            # If it cannot be completed at rate k within h hours, try values > k 
            else:
                l = k + 1
            
        return res