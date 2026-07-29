class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we want to use two pointers to get the target sum
        # we can shift the indices based on if our sum < or > or = to the target since its already sorted
        # return [index1, index2] that add up to the target

        left = 0
        right = len(numbers) - 1 

        while left <= right:
            target_sum = numbers[left] + numbers[right]

            if target_sum < target:
                left += 1 
            
            elif target_sum > target:
                right -= 1 

            else:
                return [left + 1, right + 1]
                