class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We want to count the numbers and with the count return the top k elements in a list
        # The optimal way is to use a bucket sort
        # We can count up the numbers with a hashmap
        counts = defaultdict(int)

        # dictionary = number: count -> 2: 2 
        for number in nums:
            counts[number] += 1 

        
        buckets = [[] for _ in range(len(nums) + 1)]

        # go through the hashMap
        for number, frequency in counts.items():
            buckets[frequency].append(number)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                result.append(value)

                if len(result) == k:
                    return result

