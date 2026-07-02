class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can track the difference between target and our current number in our hashMap
        # with the difference we can compare if our difference is already in the map which ends up adding up to our two sum

        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[num] = i 