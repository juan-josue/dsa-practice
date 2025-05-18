from ast import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeroes = 0
        product = 1

        # Determine product (w/o 0's) and # of 0's
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeroes += 1
            else:
                product *= nums[i]

        # If there are > 1 0's, all products will be 0
        if num_zeroes > 1:
            return [0] * len(nums) 

        # Determine products
        res = []
        for i in range(len(nums)):
            if num_zeroes == 1:
                res.append(product if nums[i] == 0 else 0)
            else:
              res.append(int(product / nums[i]))
        return res   