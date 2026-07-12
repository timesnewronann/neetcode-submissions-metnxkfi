class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Goal: Return the length of the longest secutive 
        # we can put the list into a hashSet to get the non duplicates
        hashSet = set(nums)

        # track the longest sequence
        longest = 0 

        # go through the list of numbers
        for num in nums:
            # if the previous number isn't in the hashSet
            # we are at the start of the sequence
            if (num - 1) not in hashSet:
                length = 0

                # while we are on a sequence
                while (num + length) in hashSet:
                    length += 1 

                    longest = max(length, longest)

            
        return longest