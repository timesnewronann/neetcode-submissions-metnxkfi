class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can solve this question with a bucket sort
        # we are sorting the numbers by frequencies 
        # so if a number occurs 3 times it goes in the 3 time bucket and so on

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 
        

        # make our buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                
                if len(result) == k:
                    return result