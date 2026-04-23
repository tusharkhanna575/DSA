class Solution:
    def solveNQueens(self, n):
        # your code goes here
        """
        T.C. : O(n!)
        S.C. : O(n)
        """

        def help(row, ans, board):
            if len(board) == row:
                ans.append([''.join(i) for i in board])
                return
            for col in range(len(board[0])):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    help(row+1, ans, board)
                    board[row][col] = '.'

        def is_safe(board, row, col):
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            r, c = row, col
            while r >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
            r, c = row, col
            while r >= 0 and c < len(board[0]):
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            return True

        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        help(0, ans, board)
        return ans
