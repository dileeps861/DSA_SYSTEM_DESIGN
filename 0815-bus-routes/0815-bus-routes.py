class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        adj = defaultdict(list)
        adjStop = defaultdict(set)
        q = deque()
        visited = set()
        for index, route in enumerate(routes):
            for stop in route:
                adj[stop].append(index)
                adjStop[index].add(stop)
                if source == stop:
                    q.append(index)
                    visited.add(index)
        res = 0
        while q:
            sz = len(q)
            res += 1
            while sz > 0:
                rts = q.popleft()
                if target in adjStop[rts]:
                    return res
                for stop in routes[rts]:
                    if target == stop:
                        return res
                    for route in adj[stop]:
                        if route not in visited:
                            q.append(route)
                    visited.add(route)
                sz -= 1

        return -1
