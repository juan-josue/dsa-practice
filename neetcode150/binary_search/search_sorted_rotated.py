from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        Conditions to search right:

        (a) Right is sorted - m < r
            (a1) - m < target <= r      [6,1,2,3,4,5]     target = 4
        (b) Right is unsorted - m > r 
            (b1) - m < target           [4,5,6,7,8,1,2,3] target = 8
            (b2) - target <= r          [3,4,5,6,1,2]     target = 1

        Search Left otherswise:
                                        [5,1,3]           target = 5
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m

            # Case (a) and (a1)
            if nums[m] < nums[r] and nums[m] < target <= nums[r]:
                l = m + 1
            # Case (b) and (case b1 or case b2)
            elif nums[m] > nums[r] and (nums[m] < target or target <= nums[r]):
                l = m + 1
            else:
                r = m - 1

        return -1