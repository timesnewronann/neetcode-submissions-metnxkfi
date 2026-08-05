class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can use prefix and postfix to get the products of array except self
        result = [0] * len(nums)
        prefix = 1 

        for i in range(len(nums)):
            result[i] += prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result