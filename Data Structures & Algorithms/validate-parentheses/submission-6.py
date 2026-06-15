class Solution:
    def isValid(self, s: str) -> bool:
        # map the brackets to closing to open with a hashMap
        closeToOpen = {"}": "{", ")": "(", "]": "["}

        stack = []

        for bracket in s:
            if bracket not in closeToOpen:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != closeToOpen[bracket]:
                    return False
                
                stack.pop()

        
        return not stack