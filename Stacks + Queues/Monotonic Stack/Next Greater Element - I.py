class Solution:
    def nextLargerElement(self, arr):
        """
        T.C. : O(2*n)
        S.C. : O(2*n)
        """
        n = len(arr)
        ans = [-1]*n
        st = []

        for i in range(n-1, -1, -1):
            while st and st[-1] <= arr[i]:
                st.pop()
            if not st:
                ans[i] = -1
            else:
                ans[i] = st[-1]
            st.append(arr[i])
        return ans
