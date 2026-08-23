class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use a stack to compare the temperatures
        stack = []

        # store the days of warmth in a result array
        result =[0] * len(temperatures)

        # go through each temperature
        for i in range(len(temperatures)):
            # check if the temperature is warmer
            while stack and stack[-1][0] < temperatures[i]:
                # we want to store the temperatures in our stack as a tuple (temp, index)
                # pop the stack out
                prevTemp, prevIndex = stack.pop()
                
                # store the result
                result[prevIndex] = i - prevIndex

            stack.append((temperatures[i], i))

        return result
