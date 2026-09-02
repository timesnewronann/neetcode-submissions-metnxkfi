class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can use a hashSet to track if we are on a sequence
        # first we want to place the list into set to avoid duplicates
        hashSet = set(nums)
        longest = 0 

        # go through the list
        for num in nums:
            # check if the num -1 not in hashSet (start of the sequence)
            if num - 1 not in hashSet:
                # we can track the length
                length = 0 

                while num + length in hashSet:
                    # have a sequence
                    length += 1 

                    longest = max(longest, length)

        return longest
