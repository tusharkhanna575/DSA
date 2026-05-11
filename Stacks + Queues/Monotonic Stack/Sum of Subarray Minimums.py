class Solution:

    def findNSE(self, n, arr):
        """
        T.C. : O(2*n)
        S.C. : O(2*n)
        """
        ans = [0]*n
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans

    def findPSE(self, n, arr):
        """
        T.C. : O(2*n)
        S.C. : O(2*n)"""
        ans = [0]*n
        st = []
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    def sumSubarrayMins(self, arr):
        """
        T.C. : O(5*n)
        S.C. : O(5*n)
        """
        mod = 10**9+7
        total = 0
        n = len(arr)
        nse = self.findNSE(n, arr)
        pse = self.findPSE(n, arr)
        for i in range(n):
            left = i-pse[i]
            right = nse[i]-i
            freq = left*right
            val = (freq*arr[i]) % mod
            total = (total+val) % mod
        return total
