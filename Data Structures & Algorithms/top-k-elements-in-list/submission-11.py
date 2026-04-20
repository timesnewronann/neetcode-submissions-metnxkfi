class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We want to count up all the numbers 
        # And return the top k counts

        # use a hashmap to count up the numbers
        counts = defaultdict(int)

        # build up the map
        for number in nums:
            counts[number] += 1 
        
        # build up our buckets to track the counts: number
        buckets = [[] for _ in range(len(nums) + 1)]

        # build the bucket
        for number, value in counts.items():
            buckets[value].append(number)

        # go through the buckets and store the number in the result
        result = []

        for i in range(len(buckets) -1, 0, -1):
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result


