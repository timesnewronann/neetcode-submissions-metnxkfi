class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #the sum is sorted
        #we can use two pointers
        #if the number is too small shift left up
        #if number is too big shift right down
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right+1]

            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        
