class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # O(nlog(n)) == use a merge sort

        if len(nums) <= 1:
            return nums[:]

        # calculate the middle
        middle = len(nums) // 2

        left = nums[:middle]
        right = nums[middle:]

        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)

        sorted_list = []

        i = 0 
        j = 0

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                sorted_list.append(left_sorted[i])
                i += 1 
            else:
                sorted_list.append(right_sorted[j])
                j += 1 
        
        while i < len(left_sorted):
            sorted_list.append(left_sorted[i])
            i += 1 
    
        while j < len(right_sorted):
            sorted_list.append(right_sorted[j])
            j += 1

        return sorted_list