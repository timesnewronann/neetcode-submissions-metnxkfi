class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can calculate the diff between our target and current number
        # if that difference exists in our hashmap those are the two sum numbers

        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[num] = i