class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashMap to track the diff and indexes in nums
        hashMap = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], index]
            
            hashMap[num] = index
        
        