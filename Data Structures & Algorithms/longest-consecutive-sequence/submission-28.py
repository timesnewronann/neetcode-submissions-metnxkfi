class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # GOAL is to return the length of the longest consecutive sequence of elements that can be found
        
        hashSet = set(nums)

        longest = 0 

        for num in nums:
            if num - 1 not in hashSet:
                length = 0

                while num + length in hashSet:
                    length += 1 

                    longest = max(longest, length)


        return longest