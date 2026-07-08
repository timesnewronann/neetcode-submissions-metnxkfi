class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We want to use hashmaps that track sets to keep track of our numbers in the board
        rows = defaultdict(set)

        cols = defaultdict(set)

        squares = defaultdict(set)

        # we want to go through the rows
        for row in range(9):
            # go through the cols
            for col in range(9):
                # check if we are at an empty space
                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row //3, col //3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        
        return True