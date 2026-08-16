class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # our goal is to return the list of temps with the num of days between warmer days
        # we can use a stack to compare the temperatures
        # store the (temp, index)
        stack = []

        # list of our days
        result = [0] * len(temperatures)

        # go through each temperature
        for i in range(len(temperatures)):
            # we want to only add to our result when the current temp is warmer
            while stack and stack[-1][0] < temperatures[i]:
                # we want to pop the stack off as the prevTemp, prevIndex
                prevTemp, prevIndex = stack.pop()

                # then we we want to update our result
                result[prevIndex] = i - prevIndex
            
            # add to the temp to the stack and the index
            stack.append((temperatures[i], i))

        # return the result
        return result