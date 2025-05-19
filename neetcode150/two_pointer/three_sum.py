from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):

            # Skip duplicate vals
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two Sum
            l, r = i + 1, len(nums) - 1
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                if value == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicate vals
                    left_val, right_val = nums[l], nums[r]
                    while nums[l] == left_val and l < r:
                        l += 1
                    while nums[r] == right_val and l < r:
                        r -= 1
                    
                elif value < 0:
                    l += 1
                else:
                    r -= 1

        return res

