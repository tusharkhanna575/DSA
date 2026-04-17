class Solution:

    """
    T.C. : O(n log(max(arr)))
    S.C. : O(1)
    """

    def minimiseMaxDistance(self, arr, k):

        def help(n, dist, arr):
            cnt = 0
            for i in range(1, n):
                gap = arr[i] - arr[i-1]
                cnt += int(gap / dist)
            return cnt

        n = len(arr)
        low = 0
        high = 0
        for i in range(n-1):
            high = max(high, arr[i+1]-arr[i])
        diff = 1e-6
        while ((high-low) > diff):
            mid = (low+high)/2
            cnt = help(n, mid, arr)
            if cnt > k:
                low = mid
            else:
                high = mid
        return high
