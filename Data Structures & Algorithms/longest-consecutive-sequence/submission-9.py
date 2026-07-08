class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Goal: Return length of the longest consecutive sequence of elements 
        # Each element is exactly 1 greater than the previous element

        # we can put our list of nums in a hashSet so that would remove the duplicates
        hashSet = set(nums)

        longest = 0

        # And then we can go through the list of nums
        for num in nums:
            if (num - 1) not in hashSet:
            # And check if the current number is in the hashSet <- the start of the sequence
                length = 0 
                
            # We will loop through while the current number is in the set -> to keep moving the sequence forward
                while (num + length) in hashSet:
                    length += 1 
        

                longest = max(length, longest)

        return longest