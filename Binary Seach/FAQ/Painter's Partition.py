class Solution:

    """
    T.C. : O(n logn)
    S.C. : O(1)
    """

    def minTime(self, arr, k):
        # code here
        def help(arr, maxi):
            total = 1
            unit_per_arr = 0
            for i in range(len(arr)):
                if (unit_per_arr+arr[i] <= maxi):
                    unit_per_arr += arr[i]
                else:
                    total += 1
                    unit_per_arr = arr[i]
            return total

        if (len(arr) < k):
            return -1
        low = max(arr)
        high = sum(arr)
        while (low <= high):
            mid = (low+high)//2
            chk = help(arr, mid)
            if chk > k:
                low = mid+1
            else:
                high = mid-1
        return low
