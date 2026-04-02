class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the list is sorted
        # We can use two pointers to get the two Sum
        left = 0 

        right = len(numbers) - 1 

        while left < right:
            sum_num = numbers[left] + numbers[right]

            if sum_num < target:
                # move the left pointer forward
                left += 1 
            
            elif sum_num > target:
                right -= 1 
            
            else:
                return [left + 1, right + 1]
        