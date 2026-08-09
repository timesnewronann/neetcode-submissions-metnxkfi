class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can keep track of the sequence by placing all of our numbers within a set
        hashSet = set(nums)

        # track our longest sequence
        longest = 0 

        # go through each number
        for num in nums:
            # check if we are at the start of a sequence
            if num - 1 not in hashSet:
                length = 0 

                # while we have a sequence
                while num + length in hashSet:
                    length += 1 

                    longest = max(longest, length)

        return longest