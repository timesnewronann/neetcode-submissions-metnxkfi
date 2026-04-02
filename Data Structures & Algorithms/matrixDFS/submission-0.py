class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(grid, row, col, visit):
            #all edge cases we may face
            #if the position is out of bounds
            #if the current position is already visited 
            #or we are on a blocked space
            #return 0 we can't get to the right corner
            if ( min(row,col) < 0 or row == ROWS or 
            col == COLS or 
            (row,col) in visit or 
            grid[row][col] == 1):
                return 0

            #case where we can 
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            #add the position into the set
            visit.add((row,col))

            count = 0 

            #directions of moving up down left and right
            count += dfs(grid, row + 1, col, visit) # move down
            count += dfs(grid, row - 1, col, visit) # move up
            count += dfs(grid, row, col + 1, visit) # move right
            count += dfs(grid, row, col - 1, visit) # move left

            visit.remove((row,col))
            return count

        return dfs(grid,0,0,set())
