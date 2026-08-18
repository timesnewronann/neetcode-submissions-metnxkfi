class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        # we can track our duplicate numbers with hashMaps tracking sets
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # go through each cell
        for row in range(9):
            for col in range(9):
                # check if our cell is empty
                if grid[row][col] == ".":
                    continue

                # check if we are currently on a duplicate
                if (grid[row][col] in rows[row] or 
                    grid[row][col] in cols[col] or
                    grid[row][col] in squares[(row//3, col//3)]):
                    return False
                
                # add the values into the hashMaps
                rows[row].add(grid[row][col])
                cols[col].add(grid[row][col])
                squares[(row//3, col//3)].add(grid[row][col])
            
        
        return True