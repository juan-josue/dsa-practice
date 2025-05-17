from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize number set
        num_set = set([])

        for num in nums:

            # If the number is in the set it contains a dupicates
            if num in num_set:
                return True
            num_set.add(num)
            
        return False
         