class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we can use the voting algorithm to cast votes onto the majority element
        
        # we want to track the count of the number 
        count = 0

        # and the majority result
        result = 0

        # go through each number
        for num in nums:
            # check if our current count of numbers is 0 that means we need to switch the majority count to our current number
            if count == 0:
                result = num

            # otherwise the number is the same as our results so we can keep casting votes to that number
            if num == result:
                count += 1 
            
            # otherwise it isn't the current number
            else:
                count -= 1 

        return result
