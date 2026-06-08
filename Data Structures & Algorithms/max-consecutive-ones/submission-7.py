class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        ans = 0

        for num in nums:
            if num != 1:
                ans = max(ans, curr)
                curr = 0
            else:
                curr += 1 
        
        return max(ans, curr)