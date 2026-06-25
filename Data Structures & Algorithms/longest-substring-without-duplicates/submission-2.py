class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}

        left = 0 
        ans = 0

        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(hashMap[s[right]] + 1, left)
            
            hashMap[s[right]] = right

            ans = max(ans, right - left + 1)
        
        return ans