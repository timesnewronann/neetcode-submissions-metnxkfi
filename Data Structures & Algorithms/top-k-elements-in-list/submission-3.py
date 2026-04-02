class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a bucket sort to solve this question
        # because we can contain the elements in buckets and go through it depending on the k order question asked for

        # track the frequency of the nums
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1 
        
        # create the buckets

        buckets = [ [] for _ in range(len(nums) +1)]

        for index, count in frequency.items():
            buckets[count].append(index)
        
        ans = []

        for count in range(len(nums), 0, -1):
            for bucket in buckets[count]:
                ans.append(bucket)

                if len(ans) == k:
                    return ans 
        
        return ans 