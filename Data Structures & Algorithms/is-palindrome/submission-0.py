class Solution:
    def isPalindrome(self, s: str) -> bool:
        #input is a string s
        #output will be a true false
        #We can use two pointer on this

        left = 0 
        right = len(s) - 1

        while left < right:
            #check if we're on a alphanumeric 
            while left < right and not s[left].isalnum():
                left += 1 
            while right > left and not s[right].isalnum():
                right -=1
            
            #make sure they're lower case
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True 

        return True