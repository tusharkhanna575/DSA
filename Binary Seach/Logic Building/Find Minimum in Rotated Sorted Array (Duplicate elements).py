class Solution:
    def findMin(self, arr):
        low = 0
        high = len(arr)-1
        ans = float('inf')
        while (low <= high):
            mid = (low+high)//2
            # duplicate check
            if (arr[low] <= arr[high]):
                ans = min(ans, arr[low])
                break
            if (arr[low] <= arr[mid]):
                ans = min(ans, arr[low])
                low = mid+1
            else:
                ans = min(ans, arr[mid])
                high = mid-1
        return ans
