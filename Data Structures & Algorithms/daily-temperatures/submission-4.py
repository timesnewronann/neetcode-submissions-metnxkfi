class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use a stack to keep track of the temperature
        # when we encounter a warmer temp we pop the stack pop off

        # track the days between warmer temps
        result = [0] * len(temperatures) 

        # use a stack
        stack = []

        for i in range(len(temperatures)):
            # we want to loop through while the stack isn't empty 
            # and the temp is warmer
            while stack and stack[-1][0] < temperatures[i]:
                # pop the stack
                prevTemp, prevIndex = stack.pop()

                # update the result
                result[prevIndex] = i - prevIndex

            # store the value in the stack
            stack.append((temperatures[i], i))

        return result