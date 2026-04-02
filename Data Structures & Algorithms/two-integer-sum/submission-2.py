class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # calculate the difference and store that inside a hashMap
        prevMap = {}

        # go through the numbers and look at index and values
        for index, number in enumerate(nums):
            #calculate the difference
            diff = target - number
            #check if the nums[diff] in hashMap
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[number] = index
        
        return 