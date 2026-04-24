class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a bucket sort and hashmap to count up the frequencies
        counts = defaultdict(int)

        for number in nums:
            counts[number] += 1 
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in counts.items():
            buckets[count].append(number)
        
        result = []

        for i in range(len(buckets) -1, 0, -1):
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result