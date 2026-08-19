class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can use a hashSet to track when we are on a sequence and what is a sequence
        hashSet = set(nums)

        longest = 0 

        # go through each number
        for num in nums:
            # check if we are at the start of the sequence
            if num - 1 not in hashSet:
                # track a current length variable
                length = 0

                # while we are currently on a sequence
                while num + length in hashSet:
                    length += 1 

                    longest = max(longest, length)
            
        return longest

