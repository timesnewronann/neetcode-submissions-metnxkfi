class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can get the products without using the divsion operation by tracking the prefix and postfix of the list
        # we want to get a result list of len(nums)
        result = [0] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            # set the current value to the prefix
            result[i] = prefix
            # multiply the prefix by the current number
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) -1, - 1, -1):
            # multiply the postfix to the result
            result[i] *= postfix
            
            postfix *= nums[i]

        return result