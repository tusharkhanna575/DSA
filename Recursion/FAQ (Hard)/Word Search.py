class Solution:
    def exist(self, board, word):
        # your code goes here
        """
        T.C. : O(n * m * 4^len(word))
        S.C. : O(len(word))
        """

        def help(board, i, j, word, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = ''
            ans = (help(board, i-1, j, word, k+1) or
                   help(board, i+1, j, word, k+1) or
                   help(board, i, j-1, word, k+1) or
                   help(board, i, j+1, word, k+1))
            board[i][j] = temp
            return ans

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if help(board, i, j, word, 0):
                        return True
        return False
