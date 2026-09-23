class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for bracket in s:
            if bracket in close_to_open:
                if not stack or stack[-1] != close_to_open[bracket]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(bracket)


        if len(stack) == 0:
            return True
        else:
            return False