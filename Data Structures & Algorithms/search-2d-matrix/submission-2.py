class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force solution we just go through each cell in the matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    return True

        
        return False