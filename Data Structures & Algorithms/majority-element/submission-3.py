class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0 # track the answer
        count = 0 # track our current count of elements

        for num in nums:
            # if our count is 0
            if count == 0:
                # the current majority is the number we're on
                result = num
            
            if num == result:
                # if the number we're on then increment the  total count
                count += 1 
            
            else:
                # other wise decrement it since the count decreases 
                count -= 1
        
        return result