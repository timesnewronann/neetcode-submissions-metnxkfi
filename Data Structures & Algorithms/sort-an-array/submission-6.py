class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we can use a merge sort for O(nlog(n))

        # check if the len(nums) <= 1
        if len(nums) <= 1:
            return nums[:]
        
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        # we need to calculate the middle

        # recursive call on the left side 
        left_sort = self.sortArray(left)

        right_sort = self.sortArray(right)

        result = []

        # go through the two sorted sides with two pointers
        i = 0
        j = 0

        while i < len(left_sort) and j < len(right_sort):
            if left_sort[i] < right_sort[j]:
                result.append(left_sort[i])
                i += 1 
            else:
                result.append(right_sort[j])
                j += 1 
        
        while i < len(left_sort):
            result.append(left_sort[i])
            i += 1

        while j < len(right_sort):
            result.append(right_sort[j])
            j += 1 
        
        return result