class Solution:
    def isValid(self, s: str) -> bool:
        # we can use a hashMap to track closed to open brackets
        closedToOpen = {"]": "[", "}": "{", ")": "("}

        # use a stack to add our parentheses into 
        stack = []

        # go through each bracket
        for bracket in s:
            # check if our stack is empty or or bracket isn't in the hashmap
            if bracket not in closedToOpen:
                # add the bracket into the hashmap
                stack.append(bracket)
            else:
                # check if the stack is empty or last value isn't in the map
                if not stack or stack[-1] != closedToOpen[bracket]:
                    return False
                
                stack.pop()

        return not stack