class Solution:

    def largestRectangleInHistogram(self, n, heights):
        st = []
        maxArea = 0
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                h = heights[st.pop()]
                l = st[-1] if st else -1
                width = i-l-1
                maxArea = max(maxArea, h*width)
            st.append(i)
        while st:
            h = heights[st.pop()]
            l = st[-1] if st else -1
            width = n-l-1
            maxArea = max(maxArea, h*width)
        return maxArea

    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        """
        T.C. : O(n*m)
        S.C. : O(m)
        """
        n, m = len(matrix), len(matrix[0])
        heights = [0]*m
        maxArea = 0
        for row in matrix:
            for j in range(m):
                if row[j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            maxArea = max(
                maxArea, self.largestRectangleInHistogram(m, heights))
        return maxArea
