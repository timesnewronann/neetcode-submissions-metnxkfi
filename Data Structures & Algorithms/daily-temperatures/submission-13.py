class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                prevTemp, prevIndex = stack.pop()

                # insert these into the result
                result[prevIndex] = i - prevIndex

            stack.append((temperatures[i], i))

        return result