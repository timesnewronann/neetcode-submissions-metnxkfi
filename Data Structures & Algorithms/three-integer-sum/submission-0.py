class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Return all triplets where the nums add to 0 and indices are different
        #Since the input is sorted this is like two sum ii
        #We use two pointers in that method
        #sort the input array 
        #We can run into duplicates 
        nums.sort()

        result = [] 

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue 
            left, right = index + 1, len(nums) - 1 
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    #decrease it
                    right -= 1 
                elif threeSum < 0:
                    left += 1 
                else:
                    result.append([value,nums[left],nums[right]])
                    left += 1 
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 

        return result 


