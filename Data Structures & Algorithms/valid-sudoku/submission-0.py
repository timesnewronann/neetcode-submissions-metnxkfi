class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I did this question before with Sovi
        # I remember it is 2D array traversal
        # we are given a graph so maybe need to use a dfs/bfs

        # Conditions we must follow
        # Each row must contain digits 1-9 without duplicates (makes me think of a hashSet)

        # Each column must contain digits 1-9 without duplicates (makes me think of a hashSet)

        # Each of the nine 3 x 3 sub-boxes must contain 1-9 no duplicates use a tuple of something 

        # return True or false

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                # if we are on an empty space move to the next cell
                if board[row][col] == ".":
                    continue

                # if we encounter a duplicate
                if (board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row //3 , col //3)]):
                    return False 
                
                # add the values into our sets otherwise
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        return True