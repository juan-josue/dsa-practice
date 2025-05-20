from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                res += max(max_l - height[l], 0)
                max_l = max(max_l, height[l])
            else:
                r -= 1
                res += max(max_r - height[r], 0)
                max_r = max(max_r, height[r])
        return res