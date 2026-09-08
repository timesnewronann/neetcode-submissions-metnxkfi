class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can use hashMap tracking sets to track the numbers we have in each row, col, and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # go through each row and col
        for row in range(9):
            for col in range(9):
                # check if we are on an empty space
                if board[row][col] == ".":
                    continue

                # check if the space has a duplicate
                if(board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3, col//3)]):
                    return False

                # add the value into the maps
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])

        return True
