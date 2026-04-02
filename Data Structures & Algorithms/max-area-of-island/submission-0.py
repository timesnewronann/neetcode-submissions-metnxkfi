class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #we are given a grid 0 is water and 1 is land
        #we want the max area of an island
        #getting the dimensions of the grid
        ROWS = len(grid)
        COLS = len(grid[0])

        #track the maxArea 
        maxArea = 0

        #we'll track our positions with a visitSet
        visit = set()
        #use a dfs to traverse the grid and see what is valid
        def dfs(row,col):
            #base cases to check if its valid
            #if we are out of bounds
            #if are current position is water
            #If we already visited this position
            if (
                min(row,col) < 0 or row == ROWS or col == COLS or
                grid[row][col] == 0 or (row,col) in visit
            ):
                return 0 

            #add this position into our visit set
            visit.add((row,col))

            #we want to return the dfs
            return (1 + dfs(row + 1, col)
                    + dfs(row - 1, col)
                    + dfs(row, col + 1)
                    + dfs(row, col - 1))


        #we want to go through each position in our grid
        for row in range(ROWS):
            for col in range(COLS):
                #calculate the maxArea
                maxArea = max(maxArea, dfs(row,col))

        return maxArea 
