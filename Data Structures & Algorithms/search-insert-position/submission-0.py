class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # goal return True if the the target exists in the list
        # Otherwise return the index where it should be
        # The list is sorted so we can use a binary search to go through the list
        # If the target doesn't exist then we can return the index position where it should be

        left = 0 
        right = len(nums) - 1 

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > target:
                right = middle - 1
            
            elif nums[middle] < target:
                left = middle + 1 
            
            else:
                return middle
        
        return left
            