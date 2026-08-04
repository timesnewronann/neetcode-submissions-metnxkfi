class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can use a hashMap tracking hashSet to check if we have duplicates which breaks the sudoku board
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # go through the board
        for row in range(9):
            for col in range(9):
                #check if we are on an empty space
                if board[row][col] == ".":
                    continue


                # check if we have a duplicate
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row//3, col //3)]
                ):
                    return False

                # add the space into our hashMaps
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col //3)].add(board[row][col])

        
        return True