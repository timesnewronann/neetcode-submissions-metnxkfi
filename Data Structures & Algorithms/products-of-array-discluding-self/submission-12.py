class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can use the prefix and postfix to get the products of the array
        result = [0] * len(nums)
        prefix = 1

        for num in range(len(nums)):
            result[num] += prefix
            prefix *= nums[num]

        postfix = 1

        # use the postfix and fill it in backwards
        for num in range(len(nums) -1, -1, -1):
            result[num] *= postfix
            postfix *= nums[num]

        return result

