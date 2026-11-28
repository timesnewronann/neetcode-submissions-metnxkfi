class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if we only got the nums 1 at a time we can use a hashmap
        # Store for the two ends of each run the length of that run 
        # When a new number arrives it can only join the run that ends at num -1 and the run the starts at num + 1 
        lengths = {}

        longest = 0 

        for num in nums:
            if num in lengths: # we have a duplicate move forward
                continue

            # length of the run ending left of the num
            left = lengths.get(num - 1, 0)

            # length of the run ending right of the num
            right = lengths.get(num + 1, 0)

            # the number that puts them together
            length = left + 1 + right

            # mark this num in the hashMap
            lengths[num] = length

            # update the left and right
            lengths[num - left] = length

            lengths[num + right] = length

            # update our longest
            longest = max(longest, length)

        return longest
