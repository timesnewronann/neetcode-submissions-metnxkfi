class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BruteForce we can use two for loops and compare if the two values add up
        # O(n^2) solution pretty slow
        # We can optimize this with a hashmap and check if the difference between our number and target exists
        hashMap = {}

        # go through the index, and numbers in the list
        for index, num in enumerate(nums):
            # keep track of the diff between our target and num
            diff = target - num 

            # if the difference exists in our map we can return the indexes
            if diff in hashMap:
                return [hashMap[diff], index]
            
            # store the index as a value with num as the key num: index
            hashMap[num] = index