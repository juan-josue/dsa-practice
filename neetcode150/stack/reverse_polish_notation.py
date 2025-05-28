from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = { '+', '-', '*', '/' }
        for token in tokens:
            # If we encounter an operator
            if token in operators:
                temp = s.pop()
                match token:
                    case '+':
                        temp += s.pop()
                    case '-':
                        temp = s.pop() - temp
                    case '*':
                        temp *= s.pop()
                    case '/':
                        temp = int(s.pop() / temp)
                s.append(temp)

            # If we encounter an integer
            else:
                s.append(int(token))        
        return s[-1]