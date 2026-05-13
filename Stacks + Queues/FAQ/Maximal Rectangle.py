# ---------- Using Stack & Prefix Sum ----------

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


# ---------- Using Dynamic Programming ----------

class Solution:

    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        """
        T.C. : O(n**2 * m)
        S.C. : O(n*m)
        """
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dp[i][j] = (dp[i-1][j]+1) if i > 0 else 1
                    width = dp[i][j]
                    for k in range(j, -1, -1):
                        width = min(width, dp[i][k])
                        maxArea = max(maxArea, width*(j-k+1))
        return maxArea
