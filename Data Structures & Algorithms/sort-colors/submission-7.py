class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we do a swap function on the left and right sides
        # if we encounter a 0 it goes on the left partition
        # if we encounter a 2 it goes on the right parition
        left = 0 
        right = len(nums) - 1 
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= right:
            if nums[i] == 0:
                # swap the values
                swap(left, i)
                left += 1 
            
            
            elif nums[i] == 2:
                swap(i, right)
                right -= 1 
                i -= 1 
            
            i += 1 


