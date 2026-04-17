class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can solve this with a dictionary tracking the counts of numbers
        counts = defaultdict(int)

        # build up the map of numbers: counts
        for num in nums:
            counts[num] += 1 
        
        # build up buckets which will store the counts: numbers with that count
        buckets = [ [] for _ in range(len(nums) + 1)]

        # build the bucket
        for number, count in counts.items():
            buckets[count].append(number)

        # we will track it like [[3 count: number 3], [2 count: number 2]]
        
        # we want to return the top k elements in a list
        result = []

        # go through the buckets in descending order since we want the top k
        for i in range(len(buckets) -1, 0, -1):
            # go through the buckets
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result