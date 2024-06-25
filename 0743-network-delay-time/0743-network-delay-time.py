class Solution:
    class UnionFind:
        def __init__(self, n):
            self.degree = [ 1 for _ in range(n)]
            self.root = [ i for i in range(n)]
        def find(self, u):
            if u != self.root[u]:
                self.root[u] = self.find(self.root[u])
            return self.root[u]
        def union(self, u, v):
            idxU = self.find(u)
            idxV = self.find(v)

            if idxU != idxV:
                if self.degree[idxU] > self.degree[idxV]:
                    self.root[idxV] = idxU
                elif self.degree[idxU] < self.degree[idxV]:
                    self.root[idxU] = idxV
                else:
                    self.degree[idxU] += 1
                    self.root[idxV] = idxU

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times = [(w, u , v) for u,v,w in times]
        # heapify(times)
        # res = 0
        # uf = UnionFind(n)
        # while times:
        #     w,u,v = heappop(times)

        # Single source shortest path 
        # use dijktra to solve it
        # add source with 0 cost and add all the neighbours

        # build graph
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u - 1].append((w, v - 1))
            # adj[v - 1].append((w, u - 1))
        
        pq = []
        pq.append((0, k - 1))
        visited = set()
        costs = [float("inf")] * n
        costs[k - 1] = 0

        while pq:
            w, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            for w1, v in adj[u]:
                if costs[u] + w1 < costs[v]:
                    costs[v] = costs[u] + w1
                    heapq.heappush(pq, (costs[v], v))
        max_cost = max(costs)
        return max_cost if max_cost < float("inf") else -1