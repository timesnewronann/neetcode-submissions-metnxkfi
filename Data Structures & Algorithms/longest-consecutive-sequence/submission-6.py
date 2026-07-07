class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # our goal is to return the lenght of the longest consecutive sequence
        # The seqquence is exatly 1 greater than the previous element
        # We can store the list of numbers in a hash Set
        # set = [2, 3, 4, 5, 10, 20] -> we can check the left side of an num if it it's nothing we know that's the start

        longest = 0 # tracking the longest consecutive sequence

        # we can put our list of nums in hash set
        hashSet = set(nums)

        # go through each element in the original list
        for num in nums:
            # we can check if the starter element isn't in the hash Set
            if (num - 1) not in hashSet:
                # our current sequence length
                length = 0

                # check while our current number is in the hash Set so that means we have a sequence
                while (num + length) in hashSet:
                    length += 1 
                
            
                # we can check the longest sequence
                longest = max(longest, length)

        
        return longest