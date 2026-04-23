class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # We can use two hashMaps and build up the counts of the letter
        hashMap_s = defaultdict(int)

        hashMap_t = defaultdict(int)

        for letter in s:
            hashMap_s[letter] += 1 
        
        for letter in t:
            hashMap_t[letter] += 1 
        
        # compare one hashMap's counts to the other
        for letter, count in hashMap_s.items():
            if hashMap_t[letter] != count:
                return False
            
        return True