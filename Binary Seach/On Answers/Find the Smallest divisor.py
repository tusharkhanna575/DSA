import math


class Solution:

    """
    T.C. : O(n*logn)
    S.C. : O(1)
    """

    def smallestDivisor(self, nums, limit):

        def help(arr, mid, n):
            sum = 0
            for i in range(n):
                sum += math.ceil(arr[i]/mid)
            return sum

        n = len(nums)
        if (n > limit):
            return -1
        low = 1
        high = max(nums)
        ans = -1
        while (low <= high):
            mid = (low+high)//2
            if (help(nums, mid, n) <= limit):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
