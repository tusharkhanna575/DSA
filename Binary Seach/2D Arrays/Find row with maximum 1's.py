from bisect import bisect_left


class Solution:

    """
    T.C. : O(n logn)
    S.C. : O(1)
    """

    def rowWithMax1s(self, mat):
        n = len(mat)
        m = len(mat[0])

        min_idx = m
        ans_row = -1

        for i in range(n):
            idx = bisect_left(mat[i], 1)
            if idx < m and idx < min_idx:
                min_idx = idx
                ans_row = i

        return ans_row
