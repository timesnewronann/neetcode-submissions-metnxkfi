class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths aren't the same can't be an anagram
        if len(s) != len(t):
            return False 

        # we can use two hashMap to track the counts of the two strings
        hashMap_s = defaultdict(int)
        hashMap_t = defaultdict(int)

        for letter in s:
            hashMap_s[letter] += 1
        
        for letter in t:
            hashMap_t[letter] += 1 
        

        for letter, count in hashMap_s.items():
            if count != hashMap_t[letter]:
                return False
            
        return True