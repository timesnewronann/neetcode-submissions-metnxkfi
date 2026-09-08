class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # our goal is to return the number of subarray sums that equal to k
        result = 0

        # we can approach this question by calculating the prefixSums

        # then counting up which equal to k
        # we can use a hashMap to tally up the currSum of the sequence

        currSum = 0

        prefixSums = defaultdict(int)

        prefixSums[0] = 1

        for num in nums:
            currSum += num

            # calculate the diff between our currSum and the value
            diff = currSum - k

            # add the count if the difference prefixSum exist
            # default value is 0 if nothing exists so doesn't break our code
            result += prefixSums[diff]

            # store the prefixSum count
            prefixSums[currSum] += 1 

        return result
            