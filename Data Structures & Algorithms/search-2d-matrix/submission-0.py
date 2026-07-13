class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # so a brute force solution would be to iterate through each list within the lists
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    return True
        
        return False 