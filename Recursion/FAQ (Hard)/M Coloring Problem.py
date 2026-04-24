class Solution:
    def graphColoring(self, edges, m, n):
        # your code goes here
        """
        T.C. : O(m^n)
        S.C. : O(n)
        """

        def solve(node, m, n, colors, adj):
            if n == node:
                return True
            for i in range(1, m+1):
                if is_safe(i, node, colors, adj):
                    colors[node] = i
                    if solve(node+1, m, n, colors, adj):
                        return True
                    colors[node] = 0
            return False

        def is_safe(col, node, colors, adj):
            for nei in adj[node]:
                if colors[nei] == col:
                    return False
            return True

        adj = [[]for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        colors = [0]*n
        return solve(0, m, n, colors, adj)
