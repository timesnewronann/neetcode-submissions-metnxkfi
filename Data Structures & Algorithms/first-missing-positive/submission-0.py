class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # must be O(n) and o(1)
        # Goal is to return the smallest positive integer not in nums
        # brute force approach -> we have to go through the entire list
        # and then check if the current number exists in the range
        # I guess we can put each value inside of a hashMap existing in that range
        # and whichever number has a count of 0 is the first missing positive
        # This is O(n) 
        counts = defaultdict(int)

        # go through each number is O(n)
        for num in nums:
            counts[num] += 1

        # and to go through the hashMap 
        for i in range(1, len(nums) + 2):
            if counts[i] == 0:
                return i
