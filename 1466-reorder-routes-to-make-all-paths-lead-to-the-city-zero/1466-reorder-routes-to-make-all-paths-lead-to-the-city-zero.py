class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        g = dict()
        g_in = dict()

        def buildGraph(connections):
            for u, v in connections:
                if u not in g:
                    g[u] = set()

                if v not in g_in:
                    g_in[v] = set()
                g[u].add(v)
                g_in[v].add(u)

        buildGraph(connections)
        changes = [0]

        def dfs(u, visited):
            visited.add(u)
            if u in g_in:
                for v in g_in[u]:
                    if v not in visited:
                        dfs(v, visited)
            if u in g:
                for v in g[u]:
                    if v not in visited:
                        changes[0] += 1
                        dfs(v, visited)

        dfs(0, set())
        return changes[0]
