class Solution:

    """
    T.C. : O(logn)
    S.C. : O(1)
    """

    def search(self, nums, k):
        low = 0
        n = len(nums)
        high = n-1
        while (low <= high):
            mid = (low+high)//2
            if nums[mid] == k:
                return mid
            # left sorted half
            if nums[low] <= nums[mid]:
                if nums[low] <= k <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            # right sorted half
            else:
                if nums[mid] <= k <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
