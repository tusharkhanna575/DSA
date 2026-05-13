class Solution:
    def largestRectangleArea(self, heights):
        """
        T.C. : O(2*n)
        S.C. : O(n)
        """
        n = len(heights)
        st = []
        nse = pse = 0
        maxArea = 0

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                idx = st.pop()
                pse = st[-1] if st else -1
                nse = i
                maxArea = max(maxArea, heights[idx]*(nse-pse-1))
            st.append(i)

        while st:
            nse = n
            idx = st.pop()
            pse = st[-1] if st else -1
            maxArea = max(maxArea, heights[idx]*(nse-pse-1))

        return maxArea
