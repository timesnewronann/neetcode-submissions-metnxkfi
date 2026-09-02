class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can use a prefix sum and postfix sum to get the product
        # define a result list
        result = [0] * len(nums)

        prefix = 1 

        for i in range(len(nums)):
            result[i] += prefix
            prefix *= nums[i]

        postfix = 1 

        for i in range(len(nums) - 1, - 1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result