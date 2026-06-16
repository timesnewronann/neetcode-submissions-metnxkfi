class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums[:]

        # calculate the middle
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        # recursive call on the left and right sides of the list
        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)

        merged = []

        # track the pointers 
        i = 0
        j = 0

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1
            
            else:
                merged.append(right_sorted[j])
                j += 1 
        
        # exhaust both of the lists fully
        while i < len(left_sorted):
            merged.append(left_sorted[i])
            i += 1 
        
        while j < len(right_sorted):
            merged.append(right_sorted[j])
            j += 1

        return merged
