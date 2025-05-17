from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Determine num frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Populate freq buckets
        buckets = [[] for i in range(len(nums) + 2)]
        for num in freq:
            buckets[freq[num]].append(num)
        
        # Determine Top K most frequent
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

