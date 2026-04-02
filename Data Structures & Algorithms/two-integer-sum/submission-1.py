class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find the two numbers that add up to the target 
        # return a list of the indices of the two numbers that added up 

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
