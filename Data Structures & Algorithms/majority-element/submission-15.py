class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we want to cast votes on the numbers

        # the majority element
        result = 0
        
        # the amount of times the number appears
        count = 0

        # go through each number
        for num in nums:
            #check if the count == num
            if count == 0:
                result = num

            if result == num:
                count += 1 
            
            else:
                count -= 1 
        
        return result