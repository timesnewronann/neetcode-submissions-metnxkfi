class Solution:
    def isValid(self, s: str) -> bool:
        # our goal is to check if the string is a valid parenthesis
        # We can map the parentheses close to open 
        close_to_open = {"}":"{", ")": "(", "]":"["}

        # use a stack to store the current parantheses
        stack = []

        # go through the string
        for char in s:
            # check if the bracket is an opening bracket
            if char not in close_to_open:
                stack.append(char)
            
            else:
            # If the bracket is closing
                if not stack or stack[-1] != close_to_open[char]:
                    return False
                
                # matches pop from the stack
                stack.pop()

        return not stack