from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort()

        stack = []

        for pos, spd in cars[::-1]:
            stack.append([pos, spd])
            if len(stack) > 1:
                # Determine arrival times for incoming car, and prev top of stack
                t1 = ((target - stack[-1][0]) / stack[-1][1])
                t2 = ((target - stack[-2][0]) / stack[-2][1])

                # If the incoming car's arrival time is faster,
                # it joins the fleet of the slower car (popped from stack)
                if t1 <= t2:
                    stack.pop() 

        return len(stack)