class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This a prefix sum question
        # we would set the value to 1 though since we are multiplying and getting a product

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result