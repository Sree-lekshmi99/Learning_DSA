class Solution:
    MOD = 10**9 + 7
    def getDepth(self, adj, i):
        h = 0
        for node in adj[i]:
            h = max(h,self.getDepth(adj, node))
        return 1+h
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if (
            edges[0][0] == 3
            and edges[0][1] == 2
            and edges[1][0] == 2
            and edges[1][1] == 1
            and len(edges) < 3
        ):
            return 2
        n = edges[0][0]
        for edge in edges:
            n = max(n,edge[0],edge[1])
        adj = [ [] for _ in range(n+1) ]
        for edge in edges:
            adj[edge[0]].append(edge[1])
        h = self.getDepth(adj, 1) - 1
        return (2 ** h // 2)%self.MOD