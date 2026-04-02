class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #We want to use boundaries to help solve this problem
        
        result = []

        #define our boundaries
        left = 0 
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        #go through the boundaries while they haven't crossed
        while left < right and top < bottom:
            #go through the top row from left to right
            for i in range(left, right):
                result.append(matrix[top][i])

            #shift the top pointer down
            top += 1

            #go through the right column 
            for i in range(top,bottom):
                result.append(matrix[i][right-1])

            right -= 1 #shift the right column to the left 


            #check if we have broken the loop
            if not (left < right and top < bottom):
                break

            #go throguh the bottom row right to left
            for i in range(right - 1, left - 1, - 1):
                result.append(matrix[bottom-1][i])

            bottom -= 1 #shift bottom row up 1

            #go throguh the left column bottom to top
            for i in range(bottom -1, top -1, -1):
                result.append(matrix[i][left])

            left += 1

        return result 