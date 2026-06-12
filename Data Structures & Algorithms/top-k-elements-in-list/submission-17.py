class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort question
        # We want to go through the list of nums
        # and track the counts of elements
        # Then create a list of buckets to place the top frequency
        # Then we go through the buckets backwards and add the frequencies into our 
        # result array until the length is k 

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the number and frequency of the hash<ap
        for number, count in counts.items():
            # the key for the list is the frequency and we add the number 
            buckets[count].append(number)


        result = []

        # go through the list of buckets backwards 
        for i in range(len(buckets) - 1, 0, -1):
            # go through the values in the frequency bucket
            for value in buckets[i]:
                # add the number into our list
                result.append(value)

                if len(result) == k:
                    return result