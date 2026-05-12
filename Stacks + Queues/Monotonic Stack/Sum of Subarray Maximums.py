class Solution:

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

    def sumSubarrayMaxs(self, arr):
        """
        T.C. : O(5*n)
        S.C. : O(5*n)
        """
        n = len(arr)
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
