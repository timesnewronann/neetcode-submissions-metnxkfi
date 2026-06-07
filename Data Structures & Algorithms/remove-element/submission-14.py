class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # goal: remove all occurences of value within nums list
        # brute force go through the list check if the current num == val 
        # rewrite the value to be the next number if its not value 
        left = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1 
            
        return left