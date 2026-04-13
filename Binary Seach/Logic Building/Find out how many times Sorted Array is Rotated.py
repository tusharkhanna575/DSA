class Solution:
    def findKRotation(self, nums):
        low = 0
        high = len(nums)-1
        ans = float('inf')
        idx = -1
        while (low <= high):
            mid = (low+high)//2
            if (nums[low] <= nums[high]):
                if (nums[low] < ans):
                    idx = low
                    ans = nums[low]
            if (nums[low] <= nums[mid]):
                if (nums[low] < ans):
                    idx = low
                    ans = nums[low]
                low = mid+1
            else:
                high = mid-1
                if (nums[mid] < ans):
                    idx = mid
                    ans = nums[mid]
        return idx
