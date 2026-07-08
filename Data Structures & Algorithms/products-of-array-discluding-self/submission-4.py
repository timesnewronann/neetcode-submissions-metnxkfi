class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a result array prepopulated with 1
        result = [1] * len(nums)

        # create a prefix variable
        prefix = 1 

        # go through each index in the list of nums
        for i in range(len(nums)):
            result[i] = prefix

            # update the prefix with prefix * nums[i]
            prefix *= nums[i]
        
        # now we mulitply post fix in
        postfix = 1 

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
    
        return result