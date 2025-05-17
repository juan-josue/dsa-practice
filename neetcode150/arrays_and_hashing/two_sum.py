from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            # Determine complementary number
            diff = target - num

            # If dict contains complement return indices
            if diff in num_to_index:
                return [num_to_index[diff], index]

            num_to_index[num] = index
        