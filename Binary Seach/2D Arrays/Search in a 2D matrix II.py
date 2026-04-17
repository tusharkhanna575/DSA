class Solution:

    """
    T.C. : O(n + m)
    S.C. : O(1)
    """

    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        row = 0
        col = m-1
        while (row < n and col >= 0):
            if (matrix[row][col] == target):
                return True
            if (matrix[row][col] < target):
                row += 1
            else:
                col -= 1

        return False
