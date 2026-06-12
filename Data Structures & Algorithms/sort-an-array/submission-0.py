class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # maybe we can use a merge sort 
        # divide the array into halves recursively sort each half

        if len(nums) <= 1:
            return nums[:]
        
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)

        i = 0 
        j = 0
        merged_list = []

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                merged_list.append(left_sorted[i])
                i += 1 
            else:
                merged_list.append(right_sorted[j])
                j += 1 

        while i < len(left_sorted):
            merged_list.append(left_sorted[i])
            i += 1 
        
        while j < len(right_sorted):
            merged_list.append(right_sorted[j])
            j += 1 
        
        return merged_list
