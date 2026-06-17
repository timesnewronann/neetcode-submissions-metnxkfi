class Solution:
    def isValid(self, s: str) -> bool:
        # we can solve this question by tracking the parentheses closed to open with a hashMap
        # Then using a stack to append and pop the bracket
        
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        stack = []

        for bracket in s:
            # check if the bracket is in the closeToOpen
            if bracket not in closeToOpen:
                stack.append(bracket)
            
            else:
                if not stack or stack[-1] != closeToOpen[bracket]:
                    return False
                
                stack.pop()


        return not stack