class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        #We want to use a dfs
        #We want to get the size of our grid
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(grid, row, col, visit):
            #what if the position is out of bounds
            #if our row == ROWS or col == COLS
            #is our current position already visited
            #check if were blocked
            if ( min(row,col) < 0 
            or row == ROWS or col == COLS 
            or (row,col) in visit or grid[row][col] == 1):
                return 0
            

            #if row == ROWS - 1 and col == COLS -1 
            # return 1 
            if row == ROWS - 1 and col == COLS - 1:
                return 1 

            #add the position to visit set
            visit.add((row,col))

            #count = 0 
            count = 0

            #update the count with each direction left, right, up and down
            count += dfs(grid, row + 1, col, visit) #down
            count += dfs(grid, row - 1, col, visit) #up 
            count += dfs(grid, row, col + 1, visit) # right
            count += dfs(grid, row, col - 1, visit) # left 
            #we'll remove the cell from visit

            visit.remove((row,col))
            return count 

        #return dfs
        return dfs(grid, 0,0, set())