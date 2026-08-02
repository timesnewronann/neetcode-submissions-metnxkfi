class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap_s = defaultdict(int)
        hashMap_t = defaultdict(int)

        for letter in s:
            hashMap_s[letter] += 1 

        for letter in t:
            hashMap_t[letter] += 1 
        
        for num, count in hashMap_s.items():
            if hashMap_t[num] != count:
                return False
        
        return True