class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This question is supposed to be solved with a stack
        # Maybe we can go through the list of nums and add elements
        # If the element is on the top of the stack
        # We pop it off and append the current element to remove the duplicate
        # Then the stack should have the entire duplicate free list

        # This has to be done inplace
        left = 1 

        for right in range(1, len(nums)):
            if nums[right]!= nums[right-1]:
                nums[left] = nums[right]
                left += 1 
        
        return left