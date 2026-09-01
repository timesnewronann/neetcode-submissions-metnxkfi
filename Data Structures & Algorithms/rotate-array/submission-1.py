class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # reverse the entire array
        left = 0
        right = len(nums) - 1 

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -= 1 

        # reverse the first k elements
        left = 0
        right = k - 1 
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -= 1 

        # reverse the remaining portion
        left = k
        right = len(nums) - 1 
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -=1 

