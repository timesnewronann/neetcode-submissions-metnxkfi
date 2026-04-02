class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we can try to solve this with two pointers
        # We can have a slow and fast pointer approach
        # go through the list of numbers check if i == j -> they are duplicates remove j from the list
        left = 1

        for right in range(1,len(nums)):
            #is the value at right a new value or a duplicate
            # compare our current value to the value before it 
            if nums[right] != nums[right -1]:
                nums[left] = nums[right] # place the unique value at our left index
                left += 1 # shift our pointer to the next spot 
            
        return left

            
