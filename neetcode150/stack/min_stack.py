class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Update Min Stack
        if self.minStack == [] or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

        # Update Stack
        self.stack.append(val)
            

    def pop(self) -> None:
        # Update Min Stack
        self.minStack.pop()

        # Update Stack
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
