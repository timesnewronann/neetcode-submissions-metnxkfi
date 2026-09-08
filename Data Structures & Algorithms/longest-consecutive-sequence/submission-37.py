class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can use a hashSet to track what is a current sequence
        hashSet = set(nums)

        # track the longest sequence
        longest = 0

        # go through each number
        for num in nums:
            if num - 1 not in hashSet:
                # we have a start of the sequence
                length = 0

                while num + length in hashSet:
                    length += 1 

                    longest = max(length, longest)

        return longest 