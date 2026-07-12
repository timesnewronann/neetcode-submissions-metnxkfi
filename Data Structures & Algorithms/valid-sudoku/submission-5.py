class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can use hashSets to track the numbers that we have seen already
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                # check if the current cell is empty
                if board[row][col] == ".":
                    continue
                
                # otherwise the current value is a duplicate
                elif (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col //3)]):
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row //3, col //3)].add(board[row][col])
            

        return True