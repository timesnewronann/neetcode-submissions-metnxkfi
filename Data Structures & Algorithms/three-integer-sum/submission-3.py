class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First sort the input list
        nums = sorted(nums)

        # create a result list
        result = []

        # go through each number
        for i in range(len(nums)):
            # check if the number is a duplicate and we aren't on the first index
            if i > 0 and nums[i] == nums[i -1]:
                continue

            # set our first value in the triplet
            num = nums[i]

            # set up the other two values
            left = i + 1
            right = len(nums) - 1 

            while left < right:
                target = nums[left] + nums[right]

                if target + num < 0:
                    left += 1 

                elif target + num > 0:
                    right -= 1 

                else:
                    # we need to add the values into the list and shift the left and right
                    result.append([num, nums[left], nums[right]])

                    left += 1 
                    right -=1 

                    # check if the left is on a duplicate
                    while left < right and nums[left] == nums[left -1]:
                        left += 1 

        return result 


