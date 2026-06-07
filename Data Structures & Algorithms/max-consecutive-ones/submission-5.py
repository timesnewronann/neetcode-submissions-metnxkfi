class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # what is the simplest approach
        # track the result and current count of ones
        # go through the list
        # if the number is a zero our result is what we currently have counted and restart the count
        # otherwise increment since we're at a 1
        # return them max count
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            
            else:
                count += 1 
        
        return max(count, result)