class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can go through each temperature in the list
        # process the temperature and check if the temperature is warmer than the top of the stack
        # we can then take the difference between the stack's temp and the current temp in days

        # store our initial temps
        stack = []
        
        # store the num of days between warmth
        result = [0] * len(temperatures)


        # go through each temp
        for i in range(len(temperatures)):
            # loop through while:
            # - stack isn't empty
            # - the temp is warmer

            while stack and stack[-1][0] < temperatures[i]:
                # we want to pop the stack's 
                previous_temp, previous_index = stack.pop()

                # store the result
                result[previous_index] = i - previous_index

            # add the stack as a tuple (temperature, i)
            stack.append((temperatures[i], i))

        return result