from bisect import bisect_right


class Solution:

    """
    T.C. : O(log2(10**9) * n * log2m)
    S.C. : O(1)
    """

    def findMedian(self, matrix):

        def help(matrix, n, m, x):
            cnt = 0
            for i in range(n):
                cnt += bisect_right(matrix[i], x)
            return cnt

        n, m = len(matrix), len(matrix[0])
        low, high = float('inf'), float('-inf')
        for i in range(n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m-1])
        req = (n*m)//2
        while (low <= high):
            mid = (low+high)//2
            smallEq = help(matrix, n, m, mid)
            if (smallEq <= req):
                low = mid+1
            else:
                high = mid-1
        return low
