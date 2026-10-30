class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can calculate the diff between the target and our current num
        # using a hashMap we can store that diff and it's index
        # when we arrive at a number that diff already exists in we know those are the two that sum to target
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[num] = i 
            