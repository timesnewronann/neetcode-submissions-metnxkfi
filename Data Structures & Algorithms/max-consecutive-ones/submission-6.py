class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # The brute force approach to this question
        # We have a pointer at the first value
        # we check if it is a one and then move the pointer forward
        # if the value is a 1 keep incrementing
        # once we hit a 1 save that value and into ans and reset it
        # then compare the ans and our value so on 

        curr = 0
        ans = 0

        for num in nums:
            if num != 1:
                ans = max(ans, curr)
                curr = 0 
            
            elif num == 1:
                curr += 1 
        
        return max(ans, curr)