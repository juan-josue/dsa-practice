from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) * len(matrix[0]) - 1
        rows, cols = len(matrix), len(matrix[0])
        while l <= r:
            # Determine the middle index in the 2D - Array
            mid = (l + r) // 2

            # Find the row and col of the middle index
            row = mid // cols
            col = mid % cols
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False 