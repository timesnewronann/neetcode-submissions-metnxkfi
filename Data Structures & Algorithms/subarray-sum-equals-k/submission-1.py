class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # return the total number of subarrays, sum ==k
        # so we have to get the prefix sum of each array
        # and then tally up the number of sequences
        # return the sequence

        # track the result
        result = 0

        # track the currSum of the sequence
        currSum = 0

        prefixSums = defaultdict(int)

        prefixSums[0] = 1

        for num in nums:
            currSum += num
            
            diff = currSum - k

            result += prefixSums[diff]

            prefixSums[currSum] += 1 
            
        return result