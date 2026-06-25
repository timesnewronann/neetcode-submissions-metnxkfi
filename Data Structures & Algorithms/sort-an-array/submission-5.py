class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we can solve this with a merge sort because it is in O(nLog(n))
        if len(nums) <= 1:
            return nums[:]

        middle = len(nums) // 2

        left = nums[:middle]
        right = nums[middle:]

        # recursive call
        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)


        merged = []
        i = 0 
        j = 0

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1 
            else:
                merged.append(right_sorted[j])
                j += 1 
            
        
        while i < len(left_sorted):
            merged.append(left_sorted[i])
            i += 1
        
        while j < len(right_sorted):
            merged.append(right_sorted[j])
            j += 1
        

        return merged