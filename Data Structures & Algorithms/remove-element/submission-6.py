class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # I feel like I have done this question before 
        # I think this question is a two pointer question
        # We don't actually remove the element
        # We are just tracking the remaining elements that aren't val
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1 
        
        return left
