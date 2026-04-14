import math


class Solution:
    def minimumRateToEatBananas(self, nums, h):

        def help(arr, hourly):
            total_hr = 0
            for i in range(len(arr)):
                total_hr += math.ceil(arr[i]/hourly)
            return total_hr

        low = 1
        high = max(nums)
        ans = float('inf')
        while (low <= high):
            mid = (low+high)//2
            total_hr = help(nums, mid)
            if (total_hr <= h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
