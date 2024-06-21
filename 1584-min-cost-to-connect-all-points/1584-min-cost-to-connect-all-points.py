class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n

        def find(self, u):
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

        def union(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v:
                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                elif self.rank[root_u] < self.rank[root_v]:
                    self.parent[root_u] = root_v
                else:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += 1

    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
        
        # Create all edges with their respective distances
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        # Sort edges based on distance
        edges.sort()
        
        # Initialize Union-Find structure
        uf = self.UnionFind(n)
        
        # Kruskal's algorithm to form the MST
        mst_cost = 0
        edges_used = 0
        
        for dist, i, j in edges:
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                mst_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break
        
        return mst_cost
