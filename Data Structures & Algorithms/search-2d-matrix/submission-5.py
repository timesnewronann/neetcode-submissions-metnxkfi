class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can use a binary search to check if we reached the target
        # O(log(m*n)) time
        # O(1) space

        # first we can create our grid 
        rows = len(matrix)
        cols = len(matrix[0])

        # create our left and right
        left = 0
        right = rows * cols - 1 

        while left <= right:
            # calculate the middle 
            middle = (left + right) // 2 

            # get the value
            value = matrix[middle // cols][middle % cols]

            # compare if the value < target
            # if the value is too small go to the right
            if value < target:
                left = middle + 1

            elif value > target:
                right = middle - 1

            else:
                return True

        return False
