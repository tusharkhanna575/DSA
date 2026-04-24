class Solution:
    def solveSudoku(self, board):
        # your code goes here
        """
        e = number of empty cells
        T.C. : O(9 ^ e)
        S.C. : O(e)
        """

        def solve(board):
            n = 9
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        for digit in '123456789':
                            if check(board, i, j, digit):
                                board[i][j] = digit
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True

        def check(board, row, col, digit):
            for i in range(9):
                if board[row][i] == digit or board[i][col] == digit:
                    return False
            start_row, start_col = 3*(row//3), 3*(col//3)
            for i in range(start_row, start_row+3):
                for j in range(start_col, start_col+3):
                    if board[i][j] == digit:
                        return False
            return True

        return solve(board)
