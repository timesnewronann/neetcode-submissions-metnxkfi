class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # so a brute force solution would be to iterate through each list within the lists
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == target:
        #             return True
        
        # return False 

        # we can use a binary search on the matrix

        # get the dimensions
        rows = len(matrix)

        cols = len(matrix[0])

        # pointers for first binary search
        top = 0
        bot = rows - 1 

        while top <= bot:
            row = (top + bot) // 2

            # look at the right most value
            if target > matrix[row][-1]:
                # update the row to larger value rows
                top = row + 1 
            # smaller than the smallest value in the row
            elif target < matrix[row][0]:
                bot = row - 1 
            
            else:
                # we are within the correct row and break
                break

        
        # invalid condition check

        if not (top <= bot):
            # no rows have the target value
            return False

        # second portion of the binary search
        # binary search on the current row
        row = (top + bot) // 2

        left = 0
        right = cols - 1

        while left <= right:
            middle = (left + right) // 2 

            if target > matrix[row][middle]:
                # search to the right of the row
                left = middle + 1 
            
            elif target < matrix[row][middle]:
                right = middle - 1 
            
            else:
                return True
        
        return False 



