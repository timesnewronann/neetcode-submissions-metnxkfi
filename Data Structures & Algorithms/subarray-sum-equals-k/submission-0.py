class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Goal is to return the total number of subarrays that equal to k
        
        # Maybe we use a prefix sum
        # go through each value and calculate if the sum's equal to 2
        # then for each valid subarray we update our result counter?
        # we keep track of result -> num of subarrays
        result = 0

        currSum = 0

        prefixSums = {0:1}

        # go through each value
        for num in nums:
            currSum += num

            diff = currSum - k

            result += prefixSums.get(diff, 0)

            # add to the prefix sum the currsum
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)

        return result
    