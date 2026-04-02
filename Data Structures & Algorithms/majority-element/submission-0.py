class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we can use a hashMap to count the frequency of the list 
        frequency = defaultdict(int)
        result = 0
        maxCount = 0 

        for i in nums:
            frequency[i] += 1 
            if maxCount < frequency[i]:
                result = i
                maxCount = frequency[i]
        
        return result
        
