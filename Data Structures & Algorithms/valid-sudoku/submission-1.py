class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we want to use hashSets to track the duplicate numbers
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        # go through the rows
        for row in range(9):
            # go through the cols
            for col in range(9):
                # check if the current cell is a .
                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in rows[row] 
                or board[row][col] in cols[col] 
                or board[row][col] in squares[(row // 3, col // 3)]):
                    return False


                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row // 3, col //3)].add(board[row][col])

            
        return True