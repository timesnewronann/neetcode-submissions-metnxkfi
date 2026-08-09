class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we can use a sorting algorithm to partition the left side with 0s
        # the right side with 2s
        left = 0
        right = len(nums) - 1 
        i = 0 


        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= right:
            # check if 
            if nums[i] == 0:
                # swap to the left
                swap(left, i)

                # move i forward
                left += 1 
            
            
            elif nums[i] == 2:
                # swap to the right
                swap(i, right)
                right -= 1 
                i-= 1 

            i += 1 


        