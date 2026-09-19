class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # we should map the close to open to check matches
        close_to_open = {")": "(", 
                        "]" : "[",
                        "}": "{"}

        for bracket in s:
            if bracket in close_to_open:
                if not stack or stack[-1] != close_to_open[bracket]:
                    return False
                
                stack.pop()

            else:
                stack.append(bracket)

        return len(stack) == 0