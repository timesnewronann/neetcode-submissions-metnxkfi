class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # we can do this inplace by swapping the values
        # we do the start and read
        start = 0 

        # we go through each element
        for read in range(len(nums)):
            # check if read value != 0
            if nums[read] != 0:
                # check if the read != start
                if read != start:
                    # swap these values 
                    nums[read], nums[start] = nums[start], nums[read]
                start += 1 
        
