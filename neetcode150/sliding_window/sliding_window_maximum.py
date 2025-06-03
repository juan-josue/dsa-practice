from heapq import heappop, heappush, heapify
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, heap = [], []
        heapify(heap)

        l = 0
        for r in range(0, len(nums)):
            # Add right pointer to the max heap
            heappush(heap, (-nums[r], r))

            # If the window is size is less than k
            if r - l + 1 < k:
                continue

            # Pop old max elements from the heap
            while heap[0][1] < l:
                heappop(heap) 

            # Add window maximum to res
            res.append(-heap[0][0])

            l += 1
        return res