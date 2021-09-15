import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # specialised container datatyoes under "collections"
        rows = collections.defaultdict(set) #this create a set if of keys in the rows dict
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set) # keys = (r/3, c/3) # here the keys are kept to be the integer value of row/column divided by 3 - forming the square which is 3 blocks wide and 3 blocks long
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in square[(r//3, c//3)]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r//3, c//3)].add(board[r][c])
        return True
# nums = "3,2,1".split(",") # Sample Input
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
target = 8
print (Solution().isValidSudoku(board))
