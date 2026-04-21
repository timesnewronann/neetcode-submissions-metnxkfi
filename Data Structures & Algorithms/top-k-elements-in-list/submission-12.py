class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we want to count up the elements
        # return the top k elements

        # we can use a hashMap to count the elements
        # and return the top k with buckets

        counts = defaultdict(int)

        for number in nums:
            counts[number] += 1 

        # build up a bucket to track the elements
        # [counts: numbers] -> [1:1, 2:2, 3:3] -> [1:7]
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in counts.items():
            buckets[count].append(number)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result