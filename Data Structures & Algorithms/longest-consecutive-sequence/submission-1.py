class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # goal: return the length of the longest consecutive sequence
        # What is a consecutive sequence?
        # each element is exactly 1 greater than the previous element
        # elements do not have to be consecutive in the original array
        # We would check if nums[i] 1 greater than nums[i -1]
        # ex: nums[i] == 1, nums[i + 1] == 2
        # we want to use a set to avoid having to sort this problem

        # use the set to check the next number in a sequence
        hashSet = set(nums)

        # keep track of the longest consecutive sequence
        longest = 0

        for num in nums:
            # check if it is the start of the sequence if the number doesn't point to anything on it's left
            if (num -1) not in hashSet:
                length = 0 

                # while our current number is in the set
                while (num + length) in hashSet: # check the current number
                    # keep updating our length to check the sequence
                    length += 1 
                
                longest = max(longest, length)

        return longest