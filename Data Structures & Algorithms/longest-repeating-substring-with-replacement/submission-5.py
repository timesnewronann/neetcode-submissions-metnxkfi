class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # check the changes needed = window size - most frequent character
        left = 0

        max_len = 0

        counts = defaultdict(int)

        for right in range(len(s)):
            counts[s[right]] += 1 

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1 
                left += 1 

            max_len = max(max_len, right - left + 1)

        return max_len