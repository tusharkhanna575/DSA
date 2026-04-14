class Solution:

    """
    T.C. : O(logn)
    S.C. : O(1)
    """

    def NthRoot(self, n, m):

        def help(mid, n, m):
            ans = 1
            for _ in range(1, n+1):
                ans *= mid
                if ans > m:
                    return 2
            if ans == m:
                return 1
            return 0

        low = 1
        high = m
        while (low <= high):
            mid = (low+high)//2
            mid_n = help(mid, n, m)
            if mid_n == 1:
                return mid
            elif mid_n == 0:
                low = mid+1
            else:
                high = mid-1
        return -1
