class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # you can solve this with a hashMap and shifting the start
        # when our current value in the hashMap and our start <= the hashMap index
        # our hashmap will store the letter as the key and the index it appears on as the value
        hashMap = defaultdict(int)

        # track our start of the substring
        start = 0

        # track the max_length we can get
        max_length = 0 

        # go through each value 
        for right in range(len(s)):
            # we can check if our value is in the hashMap already
            # and the index for this value is less than our start
            # we can shift our start 
            if s[right] in hashMap and hashMap[s[right]] >= start:
                # shift the new start to the index store in right plus 1 
                start = hashMap[s[right]] + 1 

            hashMap[s[right]] = right
            max_length = max(right - start + 1, max_length)

        return max_length