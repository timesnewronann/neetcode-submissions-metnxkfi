class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This is a merge sort question I think 
        # We only have 3 options right
        left = 0
        right = len(nums) - 1 


        i = 0 

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp


        while i <= right:
            # left case 
            if nums[i] == 0:
                # swap with the left pointer and i
                swap(left, i)
                left += 1 
        
            
            # right case 
            elif nums[i] == 2:
                # swap with i and right pointer
                swap(i, right)
                right -= 1 

                # if we encounter a 2 don't want to increment
                i -= 1 
            
            # increment i everytime
            i += 1 
        
        # modify the nums array in place don't need to return anything
