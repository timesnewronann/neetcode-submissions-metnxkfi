class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0 
        ans = 0 

        for number in nums:
            if number == 1:
                curr += 1 
                ans = max(curr, ans)
            
            else:
                curr = 0
        
        return ans