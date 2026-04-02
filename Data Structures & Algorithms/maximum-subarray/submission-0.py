class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #set our max sum to the first value by default
        maxSum = nums[0]

        #We'll calculate our current sum as we go through the list
        currentSum = 0
        #go through the nums list
        for num in nums:
            currentSum = max(currentSum, 0)
            #add the number in
            currentSum += num

            #compare the maxsum and the current sum
            maxSum = max(maxSum, currentSum)

        return maxSum
