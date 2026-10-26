class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I think we can optimize with a hashMap
        # we can jump past the letter if it has already been seen
        # use a hashMap to track the letter and the index it was seen in
        hashMap = defaultdict(int)

        ans = 0 
        start = 0 

        # go through the whole string
        for right in range(len(s)):
            # we should check if the letter is already in the map
            # and the current stored index >= start index
            if s[right] in hashMap and hashMap[s[right]] >= start:
                # move the start past
                start = hashMap[s[right]] + 1 

            # store the letter in the map with it's index as the value
            hashMap[s[right]] = right
            ans = max(ans, right - start + 1)

        return ans
            