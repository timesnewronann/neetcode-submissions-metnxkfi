class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # For this question we can place all of numbers in a set
        # We can check that if number in the set has it's value to the left of it
        # If it doesn't this proves that the current number is the start of a sequence
        # We can then go up by 1 and increment a counter to get the sequence length

        longest = 0

        # put all the numbers in the set -> will ignore duplicates
        hashSet = set(nums)

        # go through the original list
        for num in nums:
            # if we are the start of the sequence
            if (num - 1) not in hashSet:
                length = 0 

            # otherwise we are going to go through a sequence
            # num + length == current number
                while (num +length) in hashSet:
                    # keep incrementing the length to check the sequence
                    length += 1 
                
                longest = max(length, longest)
        
        return longest

