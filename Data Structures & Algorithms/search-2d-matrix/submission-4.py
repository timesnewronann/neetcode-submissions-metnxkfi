class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can use a binary search to determine which row and cell to search for
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2 

            if matrix[row][-1] < target:
                top = row + 1
            
            elif matrix[row][0] > target:
                bot = row - 1 
            
            else:
                break

        
        # edge case
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