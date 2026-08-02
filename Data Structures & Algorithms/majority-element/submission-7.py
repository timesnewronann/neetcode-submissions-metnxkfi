class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we can use the votes algorithm
        # what is the brute force
        # we could put all of the values in a hashMap count the elemnts
        # then sort the values and return the value with the greatest element
        nums.sort()

        return nums[len(nums) // 2]