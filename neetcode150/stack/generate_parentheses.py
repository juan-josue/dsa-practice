from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []
        def backtrack(leftBrackets, rightBrackets) -> None:
            # Base case - correct number of left and right brackets
            if leftBrackets == n and rightBrackets == n:
                res.append("".join(stack))
                return            

            # Recursive cases (2 cases)

            #  (1) Add Left Bracket
            if leftBrackets < n:
                stack.append('(')
                backtrack(leftBrackets + 1, rightBrackets)
                stack.pop()

            #   (2) Add Right Bracket
            if rightBrackets < leftBrackets:
                stack.append(')')
                backtrack(leftBrackets, rightBrackets + 1)
                stack.pop()

        backtrack(0, 0)

        return res
