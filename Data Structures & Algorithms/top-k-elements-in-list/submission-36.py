class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can do a bucket sort to get the groupings of elements
        # count up the numbers
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        # create buckets to group the numbers
        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the buckets and add up the numbers
        for num, count in counts.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
