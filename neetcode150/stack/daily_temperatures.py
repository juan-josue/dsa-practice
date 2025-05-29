class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # stores [index, temperature] pairs

        for i, temp in enumerate(temperatures):

            # While the top of the stack is lower than the incoming temp
            while stack and temp > stack[-1][1]:
                # Before popping the top, record index diff between incoming and top
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, temp])    
        return res