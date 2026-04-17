class Solution:

    """
    T.C. : O(n * log m)
    S.C. : O(1)
    """

    def findPeakGrid(self, mat):

        def maxElement(mat, n, m, col):
            maxVal = -1
            idx = -1
            for i in range(n):
                if (mat[i][col] > maxVal):
                    maxVal = mat[i][col]
                    idx = i
            return idx

        n, m = len(mat), len(mat[0])
        low, high = 0, m-1
        while (low <= high):
            mid = (low+high)//2
            row = maxElement(mat, n, m, mid)
            if mid >= 1:
                left = mat[row][mid-1]
            else:
                left = -1
            if ((mid+1) < m):
                right = mat[row][mid+1]
            else:
                right = -1
            if ((mat[row][mid] > left) and (mat[row][mid] > right)):
                return [row, mid]
            elif (mat[row][mid] < left):
                high = mid-1
            else:
                low = mid+1
        return [-1, -1]
