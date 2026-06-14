class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case where the string doesn't have the same length
        if len(s) != len(t):
            return False
            
        # use hashMap to track the counts
        hashMap_s = defaultdict(int)
        hashMap_t = defaultdict(int)

        for letter in s:
            hashMap_s[letter] += 1 
        
        for letter in t:
            hashMap_t[letter] += 1 
        

        for letter, count in hashMap_s.items():
            if hashMap_t[letter] != count:
                return False
        
        return True