from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search, but where looking for the point of infliction (a high val to low)
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = (l + r) // 2
            res = min(nums[mid], res)

            # Infliction point occurred somewhere in nums[m, r]
            if nums[mid] > nums[r]:
                l = mid + 1
            # Infliction point occurred somewhere in nums[l, m]
            else:
                r = mid - 1
        return res