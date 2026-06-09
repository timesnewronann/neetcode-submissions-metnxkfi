class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we can go through the list of numbers
        # if the current number isn't a value to remove we'll store that value inside of the index before it left
        # this will remove the element and shift the non remove values to the front

        left = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1 
        
        return left