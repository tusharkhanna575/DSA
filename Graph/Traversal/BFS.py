from collections import deque

class Solution:

    def bfs(self, node, adj, vis, ans):
        q=deque()
        q.append(node)
        while q:
            node=q.popleft()
            ans.append(node)
            for i in adj[node]:
                if not vis[i]:
                    vis[i]=True
                    q.append(i)

    def bfsOfGraph(self, V, edges):
        """
        T.C. : O(V+E)
        S.C. : O(V+E)
        """
        vis=[False]*V
        ans=[]
        adj = self.adjList(V, edges)
        for i in range(V):
            if not vis[i]:
                vis[i]=True
                self.bfs(i, adj, vis, ans)
        return ans
        

    def adjList(self, V, edges):
        adj=[[] for _ in range(V)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        return adj