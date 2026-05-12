class Solution:

    def findNSE(self, n, arr):
        ans = [0]*n
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans

    def findPSE(self, n, arr):
        ans = [0]*n
        st = []
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    def sumSubarrayMins(self, n, arr):
        mod = 10**9+7
        total = 0
        nse = self.findNSE(n, arr)
        pse = self.findPSE(n, arr)
        for i in range(n):
            left = i-pse[i]
            right = nse[i]-i
            freq = left*right
            val = (freq*arr[i])
            total = (total+val)
        return total

    def findNGE(self, n, arr):
        ans = [0]*n
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans

    def findPGE(self, n, arr):
        ans = [0]*n
        st = []
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

    def sumSubarrayMaxs(self, n, arr):
        nge = self.findNGE(n, arr)
        pge = self.findPGE(n, arr)
        total = 0
        for i in range(n):
            left = i-pge[i]
            right = nge[i]-i
            freq = left*right
            val = (freq*arr[i])
            total += val
        return total

    def subArrayRanges(self, nums):
        """
        T.C. : O(10*n)
        S.C. : O(10*n)
        """
        n = len(nums)
        return self.sumSubarrayMaxs(n, nums) - self.sumSubarrayMins(n, nums)
