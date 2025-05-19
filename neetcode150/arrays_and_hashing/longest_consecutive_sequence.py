from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set from the input array
        num_set = set(nums)

        longest_seq = 0
        for num in nums:

            # If num - 1 is not present, it is the start of a sequence 
            if num - 1 not in num_set:

                # Determine length of sequence with start == num
                seq, curr = 0, num
                while curr in num_set:
                    seq += 1
                    curr += 1

                # Update longest sequence
                longest_seq = max(seq, longest_seq)

        return longest_seq