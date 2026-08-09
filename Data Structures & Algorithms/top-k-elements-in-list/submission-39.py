class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a bucket sort to group up all the numbers with the same count
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

        # build our groups (buckets)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        result = []

        # go through the buckets in reverse order
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result