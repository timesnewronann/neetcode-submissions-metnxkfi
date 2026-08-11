class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack will store days that have not found a warmer temperature yet
        # store [temperature, index]

        stack = []
        result = [0] * len(temperatures)

        # we want the tmeps to be decreasing from bottom to top

        # While the current temp is warmer than the temp at the top of the stack
        # pop the day and calculate the answer

        for i in range(len(temperatures)):

            # while the stack is not empty and the current temp is warmer than the top of the stack
            while stack and temperatures[i] > stack[-1][0]:
                # pop the stack 
                previousTemp, previousIndex = stack.pop()

                result[previousIndex] = i - previousIndex
            
            stack.append([temperatures[i], i])

        return result


