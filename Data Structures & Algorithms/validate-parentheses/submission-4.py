class Solution:
    def isValid(self, s: str) -> bool:
        # we can use a hashmap to track closed to open brackets
        closedToOpen = {"}": "{", "]": "[", ")": "("}

        # use a stack to track the brackets
        stack = []

        for bracket in s:
            # if the bracket isn't in our hashmap 
            if bracket not in closedToOpen:
                stack.append(bracket)
            else:
                # check if the stack is empty or the last value isn't in the hashmap
                if not stack or stack[-1] != closedToOpen[bracket]:
                    return False
                
                stack.pop()
        
        return not stack