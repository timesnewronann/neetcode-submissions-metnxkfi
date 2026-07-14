class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force solution we just go through each cell in the matrix
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == target:
        #             return True

        
        # return False

        # more optimal solution 
        # we are given that the rows in matrix are sorted 
        # first integer of every row is greater than the last integer
        # So we can use a binary search to check if the row we are on would potentially contain the number
        # we use two binary searches one for the top and bottom rows and then one for left and right to search the actual row
        rows = len(matrix)
        cols = len(matrix[0])

        # create pointers for binary search
        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2
            
            # look at the right most value
            if target > matrix[row][-1]:
                # update the top row to larger values
                top = row + 1 
            
            elif target < matrix[row][0]:
                bot = row - 1 
            
            else:
                break

        
        # invalid condition check
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2 

        left = 0 
        right = cols - 1 

        while left <= right:
            middle = (left + right) // 2 

            if target > matrix[row][middle]:
                left = middle + 1 
            
            elif target < matrix[row][middle]:
                right = middle - 1 
            
            else:
                return True 

        
        return False
