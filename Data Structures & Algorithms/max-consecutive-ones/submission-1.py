class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0 
        ans = 0 

        for number in nums:
            if number == 1:
                curr += 1 
            
            else:
                ans = max(curr, ans)
                curr = 0
        
        return max(ans, curr)