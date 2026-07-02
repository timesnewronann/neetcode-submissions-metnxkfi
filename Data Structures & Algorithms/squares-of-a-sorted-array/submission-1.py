class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # we want to return the squares of each number sorted in non decreasing order
        # We can use two pointers
        left = 0
        right = len(nums) - 1

        result = [0] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            # go through this in descending order
            if abs(nums[left]) > abs(nums[right]):
                result[i] += nums[left] ** 2
                left += 1 
            
            else:
                result[i] += nums[right] ** 2
                right -= 1 
        
        return result
