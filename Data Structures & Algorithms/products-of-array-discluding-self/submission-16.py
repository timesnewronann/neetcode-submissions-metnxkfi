class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can use a prefix and postfix to build up the resulting array
        result = [0] * len(nums)
        # track our postfix
        prefix = 1

        # go through the list 
        for i in range(len(nums)):
            result[i] += prefix
            prefix *= nums[i]
        
        postfix = 1

        # go through the list backwards for the postfix
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]


        # return the result
        return result