class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can use hashMaps tracking sets to check the duplicates
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # go through the grid
        for row in range(9):
            for col in range(9):
                # check if we're on an empty space
                if board[row][col] == ".":
                    continue

                # check if we have a duplicate 
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or 
                    board[row][col] in squares[(row//3, col //3)]):
                    return False
                
                # add the space in
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])


        # if we are able to add all the squares it's a valid board
        return True