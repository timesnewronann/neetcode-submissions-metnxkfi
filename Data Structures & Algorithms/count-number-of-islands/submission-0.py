class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #We want to use a dfs on the whole grid 
        #on the dfs we want to check for these cases:
        #If we are out of bounds 
        #If we already visited the cell
        #If we are valid 
        #Edge case what if the grid is empty or we aren't on the grid 
        if not grid or not grid[0]:
            return 0 

        #Get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        #create a set that keeps track if we already visited the set
        visit = set()

        #we need to return the number of islands
        num_islands = 0

        def dfs(row,col):
            #We want to check 
            #Check if we are out of bounds, invalid cell or already visited
            if (
                row not in range(rows) or col not in range(cols) or
                (row,col) in visit or grid[row][col] == "0"
            ):
                return #go to the next cell

            #add every cell we visited
            visit.add((row,col))

            #We can go up,down,left, and right
            directions = [
                [0,1], [0,-1], [1,0], [-1,0]
            ]

            #go through every possible directions
            for dr, dc in directions:
                #call your dfs on this 
                dfs(row + dr, col + dc)

        #go through the grid
        for row in range(rows):
            for col in range(cols):
                #check if the cell is land
                if grid[row][col] == "1" and (row,col) not in visit:
                    num_islands += 1
                    #call dfs to go to next cell
                    dfs(row,col)

        return num_islands


