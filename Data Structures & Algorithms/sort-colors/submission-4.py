class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This can be solved with a heap sort 
        # I think we use partitions and a swap helper function
        left = 0 
        right = len(nums) - 1 

        i = 0

        def swap(left, right):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

        
        # we can use a partition
        while i <= right:
            if nums[i] == 0:
                # swap with the left pointer and i
                swap(left, i)
                left += 1
            
            elif nums[i] == 2:
                swap(i, right)
                right -= 1 
            
                i -= 1 

            
            i += 1

            
