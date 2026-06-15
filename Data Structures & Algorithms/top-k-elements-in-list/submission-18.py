class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a bucket sort to organize the frequency of elements into buckets 
        # so we'd have all the numbers that occur 2 times in one group 3 times etc 
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

        buckets = [[] for _ in range(len(nums) + 1)]

        # build up the buckets
        for num, count in counts.items():
            buckets[count].append(num)

        result = []
        

        # we'll go through the list in descending order 
        for i in range(len(buckets) -1, 0, -1):
            for number in buckets[i]:
                result.append(number)

                if len(result) == k:
                    return result