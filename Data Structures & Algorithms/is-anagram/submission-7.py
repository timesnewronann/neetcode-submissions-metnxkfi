class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can count up the total characters in each string
        # store the count in hashmaps 
        # compare if the counts are the same

        if len(s) != len(t):
            # edge case if the two strings aren't the same can't be an anagram
            return False 

        # fixed alphabet list 
        frequency = [0] * 26

        for i in range(len(s)):
            frequency[ord(s[i]) - ord('a')] += 1 
            frequency[ord(t[i]) - ord('a')] -= 1

        for value in frequency:
            if value != 0:
                return False 
        
        return True 