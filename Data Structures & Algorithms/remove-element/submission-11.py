class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # I have done this question before
        # it is a two pointer question I believe
        # Left tracks where the next valid element should be
        # Go through the array and when we find an element that != val write the value into the left position and move it forward
        # Everything before left contains the valid elements

        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1 
        
        return left