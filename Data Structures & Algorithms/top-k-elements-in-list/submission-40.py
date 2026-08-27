class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a bucket sort to solve this question
        # first we can count the numbers 
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

        # go through the nums and create buckets to sort by frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the hashmap
        for num, count in counts.items():
            buckets[count].append(num)

        result = []

        # go through the buckets
        for i in range(len(buckets) -1 , -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

