class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = {}
        adj = {i: [] for i in range(n)}
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        costs = [float("inf")] * n
        costs[src] = 0
        q = []
        heapq.heappush(q, (0, src, 0))
        while q:
            cost, node, stops = heapq.heappop(q)
            if k < stops - 1 or stops > costs[node]:
                continue
            costs[node] = stops
            if node == dst:
                return cost
            if node not in adj:
                continue
            for nextNode, price in adj[node]:
                nextCost = cost + price
                if stops < costs[nextNode] or stops + 1 <= k:
                    heapq.heappush(q, (nextCost, nextNode, stops + 1))
        return -1
