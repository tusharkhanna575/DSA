class Solution:
    def celebrity(self, mat):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        n = len(mat)
        top, down = 0, n-1
        while top < down:
            if mat[top][down] == 1:
                top += 1
            elif mat[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1
        if top > down:
            return -1
        for i in range(n):
            if i == top:
                continue
            if mat[top][i] == 1 or mat[i][top] == 0:
                return -1
        return top
