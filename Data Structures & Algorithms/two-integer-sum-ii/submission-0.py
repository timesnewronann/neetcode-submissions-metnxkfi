class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            #check if this is the target
            if sum == target:
                return [left +1, right +1]
            elif sum > target:
                #move the right pointer down
                right -= 1
            elif sum < target:
                left += 1
