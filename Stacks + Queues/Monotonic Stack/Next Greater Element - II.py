class Solution:
    def nextGreaterElements(self, arr):
        """
        T.C. : O(4*n)
        S.C. : O(3*n)
        """
        n = len(arr)
        ans = [-1]*n
        st = []

        for i in range(2*n-1, -1, -1):
            while st and st[-1] <= arr[i % n]:
                st.pop()
            if i < n:
                if not st:
                    ans[i] = -1
                else:
                    ans[i] = st[-1]
            st.append(arr[i % n])

        return ans
