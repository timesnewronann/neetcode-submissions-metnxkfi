class Solution:
    def isValid(self, s: str) -> bool:
        # I think we can use a hashMap to map the closed to open parentheses 
        closedToOpen = {"}": "{", "]": "[", ")": "("}

        stack = [] 
        # we can then go through the characters in the string
        for bracket in s:
            if bracket not in closedToOpen:
                stack.append(bracket)
            
            else:
                # if the bracket is a closing brace
                if not stack or stack[-1] != closedToOpen[bracket]:
                    return False


                stack.pop()

        return not stack
