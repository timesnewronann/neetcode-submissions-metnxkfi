class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we want to use prefixes and postfixes to get the products of array except self
        # track the products with a list
        result = [0] * len(nums)

        prefix = 1 

        for i in range(len(nums)):
            result[i] += prefix
            prefix *= nums[i]

        # use a postfix to get the values not filled
        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]


        return result