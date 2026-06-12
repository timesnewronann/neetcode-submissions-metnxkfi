class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can use a hashMap to track the difference between our number and target
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[n] = i
        
        