class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can count up the total characters in each string
        # store the count in hashmaps 
        # compare if the counts are the same

        if len(s) != len(t):
            # edge case if the two strings aren't the same can't be an anagram
            return False 

        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for char in s:
            hashmap_s[char] += 1 
        
        for char in t:
            hashmap_t[char] += 1 
        

        for char, count in hashmap_s.items():
            if count != hashmap_t[char]:
                return False
        
        return True 