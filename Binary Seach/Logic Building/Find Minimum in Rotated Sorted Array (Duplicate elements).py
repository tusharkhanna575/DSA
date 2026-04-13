from typing import List


class Solution:
    def findMin(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        ans = float('inf')
        while (low <= high):
            mid = (low+high)//2
            # duplicate check
            if arr[low] == arr[mid] == arr[high]:
                ans = min(ans, arr[mid])
                low += 1
                high -= 1
                continue
            if (arr[low] <= arr[mid]):
                ans = min(ans, arr[low])
                low = mid+1
            else:
                ans = min(ans, arr[mid])
                high = mid-1
        return ans
