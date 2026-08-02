class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We can use a merge sort on this question, we only have 3 options

        # we need to do a swap 
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
                swap(left, i)

                # increment left by 1 
                left += 1 

            # right case 
            elif nums[i] == 2:
                swap(i, right)
                
                # decrement right
                right -= 1 
                
                # decrement i 
                i -= 1 
            
            # always increment i
        
            i += 1 


        

