class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort question
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 
        
        # track our buckets to track the frequency of which numbers occur so a bucket will be like 3 count 2 count etc
        buckets = [[] for _ in range(len(nums) + 1)]

        # build up our bucket
        for num, count in counts.items():
            buckets[count].append(num)
        
        result = []

        # go through the buckets in descending order
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result