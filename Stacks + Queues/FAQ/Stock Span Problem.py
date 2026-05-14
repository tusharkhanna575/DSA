class Solution:

    def findPGE(self, n, arr):
        ans = [0]*n
        st = []
        for i in range(n):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            ans[i] = -1 if not st else st[-1]
            st.append(i)
        return ans

    def stockSpan(self, arr, n):
        """
        T.C. : O(2*n)
        S.C. : O(n)
        """
        ans = [0]*n
        pge = self.findPGE(n, arr)
        for i in range(n):
            ans[i] = i-pge[i]
        return ans
