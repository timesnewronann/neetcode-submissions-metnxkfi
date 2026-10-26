class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I think we can use a hashSet to check if the letter has already appeared
        left = 0 
        ans = 0 
        hashSet = set()

        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1 

            hashSet.add(s[right])
            ans = max(ans, right - left + 1)

        return ans

