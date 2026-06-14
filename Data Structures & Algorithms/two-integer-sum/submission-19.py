class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary to track the differnce between the target and number were on
        hashMap = {}

        for i , num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[num] = i