class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we can use a swap function to rearrange the colors
        # we need a left pointer
        left = 0
        # a right to swap
        right = len(nums) - 1 

        # a pointer to track our current index
        i = 0

        # create a swap helper function
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        
        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1 
            
            elif nums[i] == 2:
                swap(i, right)
                right -= 1 
                i -= 1 
            
            i += 1 
        
        
