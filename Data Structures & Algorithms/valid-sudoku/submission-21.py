class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we want to check for duplicates which would break the board
        # we can use a hashmap of sets
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                # check if we are on an empty space
                if board[row][col] == ".":
                    continue
                
                # check if the current space is a duplicate
                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row //3, col //3)]):
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col //3)].add(board[row][col])

        return True