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

        # go through the number and frequency
        for number, count in counts.items():
            buckets[count].append(number)


        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result