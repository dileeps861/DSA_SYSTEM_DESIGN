class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # Create graph and reversed graph
        g = defaultdict(list)
        g_rev = defaultdict(list)

        for u, v in connections:
            g[u].append(v)
            g_rev[v].append(u)

        def dfs(u, visited):
            changes = 0
            visited.add(u)

            # Check the reverse edges (these are the correct direction)
            for v in g_rev[u]:
                if v not in visited:
                    changes += dfs(v, visited)

            # Check the actual directed edges (we might need to reverse them)
            for v in g[u]:
                if v not in visited:
                    changes += 1 + dfs(v, visited)

            return changes

        # Start DFS from node 0
        visited = set()
        return dfs(0, visited)
