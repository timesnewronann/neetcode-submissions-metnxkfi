class Solution:
    def isPalindrome(self, s: str) -> bool:
        # this is the one we use .isalnum()

        # we use two pointers one at the start of the list and the other at the end of the list
        # we check if the value is the same at each index 
        # then we shift the pointers toward each other
        # I think we have to do a check of .isalnum and .lower() to compare the values
        left = 0 
        right = len(s) - 1 

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1 
            while left < right and not s[right].isalnum():
                right -= 1 

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1 
                right -=1 

        
        return True