class Solution:

    """
    T.C. : O(logn)
    S.C. : O(1)
    """

    def searchMatrix(self, mat, target):
        n, m = len(mat), len(mat[0])
        low = 0
        high = (m*n)-1
        while (low <= high):
            mid = (low+high)//2
            row = mid//m
            col = mid % m
            if (mat[row][col] == target):
                return True
            elif (mat[row][col] < target):
                low = mid+1
            else:
                high = mid-1
        return False
