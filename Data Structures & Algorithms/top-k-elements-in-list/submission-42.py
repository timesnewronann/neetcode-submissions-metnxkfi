class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a bucket sort to sort the frequencies
        # first count the nums in a hashMap
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 
        
        # create our buckets to track frequencies
        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the counts
        for num, count in counts.items():
            # store the num and use count as the key
            buckets[count].append(num)

        # return a list of frequent elements
        result = []

        # go through the buckets backwards
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result