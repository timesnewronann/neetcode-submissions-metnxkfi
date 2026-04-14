from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case if the lengths of the string are different
        if len(s) != len(t):
            return False

        # I think we can use a counter and ord(c) as a more optimal solution but I found storing the strings in hashMaps is easier to understand
        hashMap_s = defaultdict(int)
        hashMap_t = defaultdict(int)

        for letter in s:
            # build up the dict
            hashMap_s[letter] += 1 
        
        for letter in t:
            hashMap_t[letter] += 1 
        

        for letter, count in hashMap_s.items():
            if count != hashMap_t[letter]:
                return False
            
        return True
