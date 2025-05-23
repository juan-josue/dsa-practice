class Solution:
    def isValid(self, s: str) -> bool:
        # Map opening to closing
        d = { '{' : '}', '(' : ')', '[' : ']'}
        stack = []

        for char in s:
            if char in d.keys():
                stack.append(char)
            else:
                # If the top of the stack does not contain the opening char, return False
                if not stack or char != d[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return stack == []