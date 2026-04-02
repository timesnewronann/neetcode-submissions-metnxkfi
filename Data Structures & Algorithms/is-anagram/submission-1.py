from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edge case if the string lengths aren't the same
        if len(s) != len(t):
            return False 
            
        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)

        #build up the map with string of s
        for character in s:
            hashMapS[character] += 1
        
        for character in t:
            hashMapT[character] += 1

        for character, value in hashMapS.items():
            if value != hashMapT[character]:
                return False
        
        return True
        