class Solution:
    def findPath(self, grid):
        # your code goes here
        """
        T.C. : O(4^(n*2))
        S.C. : O(n*2)"""

        def path(m, x, y, dir, n):
            if (x == (n-1) and y == (n-1)):
                res.append(dir)
                return
            if m[x][y] == 0:
                return
            m[x][y] = 0
            if x > 0:
                path(m, x-1, y, dir+'U', n)
            if y > 0:
                path(m, x, y-1, dir+'L', n)
            if x < (n-1):
                path(m, x+1, y, dir+'D', n)
            if y < (n-1):
                path(m, x, y+1, dir+'R', n)
            m[x][y] = 1

        n = len(grid)
        res = []
        if grid[0][0] == 0 or grid[n-1][n-1] == 0:
            return res
        path(grid, 0, 0, '', n)
        return sorted(res)
