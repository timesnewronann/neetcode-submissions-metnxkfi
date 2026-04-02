class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the list of numbers isn't sorted so we can use a hashMap to track the diff
        hashMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[num] = i 
        return 