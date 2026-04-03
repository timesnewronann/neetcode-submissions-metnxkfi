class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Constraint product of all elements < k
        # We can use a sliding window to build this

        if k <= 1:
            return 0

        left = 0 
        curr = 1 # since this is a product we should start with curr as 1
        ans = 0 

        for right in range(len(nums)):
            curr *= nums[right]

            while curr >= k:
                curr //= nums[left]
                left += 1 
            
            
            ans += right - left + 1

        return ans 
