class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # check if the list is empty
        if len(nums) == 0:
            return 0

        start = 1

        for i in range(1, len(nums)):
            # how do we determine if we keep
            # if the value is not a duplicate
            if nums[i] != nums[i -1]:
                # place this value where the start index is
                nums[start] = nums[i]
                start += 1 

        return start