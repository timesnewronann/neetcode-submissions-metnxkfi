class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can use a hashSet to track the non duplicates
        # the start of a sequence can be determine by checking if the num - 1 exists in the set
        hashSet = set(nums)

        max_length = 0

        for num in hashSet:
            if num - 1 not in hashSet:
                # we have the start of the sequence track the length
                # use the length to iterate through the nums
                length = 0 

                while num + length in hashSet:
                    length += 1 
                
                max_length = max(length, max_length)

        return max_length