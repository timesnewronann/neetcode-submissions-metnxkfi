class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can solve this with a bucket sort
        # we want to use a hashmap to count the frequencies
        counts = defaultdict(int)

        # go through each number and build our initial count dict
        for number in nums:
            counts[number] += 1 
        
        # build a list for our buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the number and frequency in our dictionary
        for number, count in counts.items():
            buckets[count].append(number)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result