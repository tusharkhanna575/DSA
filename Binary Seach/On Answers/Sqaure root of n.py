class Solution:

    """
    T.C. : O(logn)
    S.C. : O(1)
    """

    def floorSqrt(self, n: int) -> int:
        if n <= 1:
            return n
        low = 1
        high = n-1
        while (low <= high):
            mid = (low+high)//2
            if ((mid**2) <= n):
                low = mid+1
            else:
                high = mid-1
        return high
