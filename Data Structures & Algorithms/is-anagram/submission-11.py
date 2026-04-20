class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we have an edge case where the strings are not the same length
        if len(s) != len(t):
            return False

        # we could use a counter but I will build up two maps 
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
