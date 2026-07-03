class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # I think we can use two pointers
        # if the left == value in right we have a duplicate we need to remove it
        # 
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1 
            
        return left
