class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()

        left = 0

        max_len = 0 

        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1 


            hashSet.add(s[right])
            max_len = max(right - left + 1, max_len)

        return max_len
        