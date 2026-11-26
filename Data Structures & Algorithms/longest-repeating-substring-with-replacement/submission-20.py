class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # letters to replace = window length - count of hte most common letter in the window
        # we can use a dictionary to track our count of letters
        hashMap = defaultdict(int)

        # track the longest value
        longest = 0
        left = 0 

        # go through the entire string
        for right in range(len(s)):
            hashMap[s[right]] += 1 

            # update our window when window size - max value > k
            while right - left + 1 - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1 
                left += 1 
            
            longest = max(right - left + 1, longest)

        return longest