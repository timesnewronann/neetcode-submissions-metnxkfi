class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Brute force we can loop through the list once to get the 1s 
        # Have a secondary loop to move the pointer and compare the lengths of the consecutive 1
        # More optimal we can keep track of curr 1's and once we encounter a non 1 we take the current max consecutive 1s and reset the counter

        curr = 0
        ans = 0

        for num in nums:
            if num != 1:
                ans = max(ans, curr)
                curr = 0
            else:
                curr += 1 
            
        return max(ans, curr)