class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # constraint is the longest substring without duplicates
        # no duplicates = use a hashSet
        # substring = sliding window

        left = 0 
        ans = 0

        hashSet = set()

        for right in range(len(s)):
            while s[right] in hashSet:
                # remove the left value 
                hashSet.remove(s[left])
                left += 1 
            
            hashSet.add(s[right])

            ans = max(ans, right - left + 1)
        
        return ans 

            