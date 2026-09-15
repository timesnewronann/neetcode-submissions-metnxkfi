class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # WE can count up for s and count down for t in the same map
        # if they're anagrams everything lands back at zero

        # one map instead of two
        # final check is anything non-zero

        # complexity O(n) time and O(1) space

        if len(s) != len(t):
            return False

        hashMap = defaultdict(int)

        for letter in s:
            hashMap[letter] += 1 

        for letter in t:
            hashMap[letter] -= 1 

        # check if anything is non zero

        for letter, count in hashMap.items():
            if count != 0:
                return False


        return True