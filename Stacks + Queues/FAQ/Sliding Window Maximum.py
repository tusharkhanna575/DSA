from collections import deque


class Solution:
    def maxSlidingWindow(self, arr, k):
        """
        T.C. : O(n)
        S.C. : O(k) + (n - k)
        """
        n = len(arr)
        ans = []
        dq = deque()
        for i in range(n):
            if dq and dq[0] <= (i-k):
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if (i >= (k-1)):
                ans.append(arr[dq[0]])
        return ans
