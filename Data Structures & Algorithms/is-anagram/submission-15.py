class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        # we can use two hashmaps and compare the counts of the letters
        hashMap_s = defaultdict(int)

        hashMap_t = defaultdict(int)

        for letter in s:
            hashMap_s[letter] += 1 
    
        for letter in t:
            hashMap_t[letter] += 1 
        
        # go through one of the maps

        for letter, count in hashMap_s.items():
            if hashMap_t[letter] != count:
                return False

        return True