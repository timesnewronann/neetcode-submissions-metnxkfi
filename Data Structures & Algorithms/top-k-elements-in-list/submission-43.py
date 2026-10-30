class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I think we can use a bucket sort for this question
        # I think what we are supposed to do is group the elements by the counts
        # first we can create a hashMap counting the elements in nums
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1 

        # then we'll create a bucket to track the frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the buckets 
        for num, counts in counts.items():
            buckets[counts].append(num)
        
        result = []

        # go through buckets backwards
        for i in range(len(buckets) - 1, - 1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

            