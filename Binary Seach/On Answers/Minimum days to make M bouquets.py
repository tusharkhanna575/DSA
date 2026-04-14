class Solution:

    """
    T.C. : O(n*logn)
    S.C. : O(1)
    """

    def roseGarden(self, n, nums, k, m):

        def possible(n, arr, day, m, k):
            cnt = 0
            no_of_bouquets = 0
            for i in range(n):
                if (arr[i] <= day):
                    cnt += 1
                else:
                    no_of_bouquets += cnt//k
                    cnt = 0
            no_of_bouquets += cnt//k
            if (no_of_bouquets >= m):
                return True
            return False

        low = min(nums)
        high = max(nums)
        if (n < m*k):
            return -1
        while (low <= high):
            mid = (low+high)//2
            if possible(n, nums, mid, m, k):
                high = mid-1
            else:
                low = mid+1
        return low
