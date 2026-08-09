class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we can use a pointer to shift the right values to where our left is
        left = 0 

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1 

        return left