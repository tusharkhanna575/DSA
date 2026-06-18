
class Solution:

    def dfs(self, node, adj, vis, ans):
        vis[node]=True
        ans.append(node)
        for i in adj[node]:
            if not vis[i]:
                self.dfs(i, adj, vis, ans)

    def dfsOfGraph(self, V, edges):
        """
        T.C. : O(V+E)
        S.C. : O(V+E)
        """
        vis=[False]*V 
        ans=[]
        adj=self.adjList(V, edges)

        for i in range(V):
            if not vis[i]:
                self.dfs(i, adj, vis, ans)
        return ans
    

    def adjList(self, V, edges):
        adj=[[] for _ in range(V)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        return adj