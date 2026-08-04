class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we want to swap the 0s to the left and the 2s to the right
        # we'll use partioning to solve this question
        left = 0
        right = len(nums) - 1 

        i = 0


        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        while i <= right:
            # if the value is a 0 swap it to the left side
            if nums[i] == 0:
                swap(left, i)

                # move left forward
                left += 1 

            
            elif nums[i] == 2:
                swap(i, right)

                # move the right down 1
                right -= 1 

                i -= 1 

            # always move i forward
            i += 1 

            
