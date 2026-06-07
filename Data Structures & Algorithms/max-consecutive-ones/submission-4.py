class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # what is the simplest approach
        # we have a two pointers
        # we start the pointer at index 1 and check if the next pointer is a 1
        # if it isn't we move the left pointer to the right
        result = 0
        count = 0

        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            
            else:
                count += 1 
        
        return max(count, result)