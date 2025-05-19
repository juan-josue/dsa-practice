from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0

        # Greedy approach
        i, j = 0, len(heights) - 1
        while i < j:
            # Calculate area
            area = (j - i) * min(heights[i], heights[j])
            highest = max(area, highest)

            # Move pointers in a Greedy way (smallest bar moves)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return highest