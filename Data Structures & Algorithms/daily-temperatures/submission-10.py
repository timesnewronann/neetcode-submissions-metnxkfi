class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use stack to compare the temperatures
        stack = []
        # stack will store (prevTemp, prevIndex)
        result = [0] * len(temperatures)

        # go through the indexes in the temps
        for i in range(len(temperatures)):
            # compare the current top of stack temp and the current temp
            while stack and stack[-1][0] < temperatures[i]:
                # pop the values on the stack
                prevTemp, prevIndex = stack.pop()

                result[prevIndex] = i - prevIndex

            stack.append((temperatures[i], i))
        

        return result

