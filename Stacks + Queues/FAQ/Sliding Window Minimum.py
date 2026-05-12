class Solution:
    def minSlidingWindow(self, arr, k):
        """
        T.C. : O(n)
        S.C. : O(k)
        """
        n = len(arr)
        ans = []
        st = []

        for i in range(n):
            while st and st[-1] > arr[i]:
                st.pop()
            st.append(arr[i])
            if i >= k-1:
                ans.append(st[0])
                if st[0] == arr[i-k+1]:
                    st.pop(0)

        return ans
