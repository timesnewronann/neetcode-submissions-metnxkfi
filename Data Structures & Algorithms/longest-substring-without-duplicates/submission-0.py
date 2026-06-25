class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I think we can create a hashSet for the letters we've already seen
        # and we would use a sliding window to track the substring

        left = 0
        seen = set()

        ans = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1 
                
            seen.add(s[right])
            ans = max(right - left + 1, ans)
        
        
        return ans
            
