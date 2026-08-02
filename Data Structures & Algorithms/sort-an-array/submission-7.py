class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we can do a merge sort o(nLog(n)) -> optimal would be a heapSort
        # first check if the length of nums <= 1

        # base case 
        if len(nums) <= 1:
            return nums[:]

        # calculate the middle
        middle = len(nums) // 2

        # get the left and right sections
        left = nums[:middle]
        right = nums[middle:]

        # we want to sort the left and right sides
        left_sorted = self.sortArray(left)

        right_sorted = self.sortArray(right)

        result = []

        i = 0

        j = 0

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                result.append(left_sorted[i])
                i += 1 
            
            else:
                result.append(right_sorted[j])
                j += 1 
        
        while i < len(left_sorted):
            result.append(left_sorted[i])
            i += 1 
        
        while j < len(right_sorted):
            result.append(right_sorted[j])
            j += 1 
        

        return result