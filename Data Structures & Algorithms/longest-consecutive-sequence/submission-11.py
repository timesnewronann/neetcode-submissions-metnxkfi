class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # goal is to return the length of the longest consecutive sequence of elements
        # The sequence has to be 1 greater between elements

        # we can create a hashSEt with all of the nums
        hashSet = set(nums)

        # keep track of the longest count
        longest = 0

        for num in nums:
            # if we are at the start of a sequence
            if (num - 1) not in hashSet:
                length = 0 # current length 

                # while we are in a sequence
                while num + length in hashSet:
                    length += 1 
                

                longest = max(length, longest)

        return longest