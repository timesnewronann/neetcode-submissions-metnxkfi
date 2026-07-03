class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we want the k most frequent elements
        # We can use a bucket sort to group the frequencies together
        
        # first we want to get the counts of each number
        counts = defaultdict(int)

        # go through the list
        for num in nums:
            counts[num] += 1

        # we want to create our buckets to group 
        buckets = [ [] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        result = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
