class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can use a hashSet to track the numbers and find the sequence
        longest = 0 
        hashSet = set(nums)

        for num in nums:
            if num - 1 not in hashSet:
                length = 0

                while num + length in hashSet:
                    length += 1 

                    longest = max(longest, length)

        return longest