class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # WE can count up for s and count down for t in the same map
        # if they're anagrams everything lands back at zero

        # one map instead of two
        # final check is anything non-zero

        # complexity O(n) time and O(1) space

        return sorted(s) == sorted(t)