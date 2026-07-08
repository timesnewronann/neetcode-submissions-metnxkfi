class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Goal is to return the k most frequent elements within the array
        # We can use a bucket sort to group the elements by frequency
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 
        
        # we can build up our buckets to sort by frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        result = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
