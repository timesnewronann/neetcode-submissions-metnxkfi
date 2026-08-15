class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Okay so we can solve this in a similar fashion/pattern to the asteroids question
        # we want to return a list of the days between warmer temps

        result = [0] * len(temperatures)

        # we can use a stack to pop off temperatures when we encounter something warmer
        stack = []

        # go through the indicies of the temperatures
        for i in range(len(temperatures)):
            # we only want to loop through our stack and build the result if we encounter a warmer temp than the top of our stack
            # store the [temperature, index]
            while stack and temperatures[i] > stack[-1][0]:
                # store the previous temp and the previous index from our stack
                previous_temp, previous_index = stack.pop()

                # store the days between inside of our result array
                result[previous_index] = i - previous_index 

            
            # store the new temp in our stack
            stack.append((temperatures[i], i))

        return result