class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def buildAdj():
            adj = defaultdict(set)
            for u, v in edges:
                adj[u].add(v)
                adj[v].add(u)
            return adj

        visited = defaultdict(int)

        def dfs(u, p):
            if visited[u] == 2:
                return False

            visited[u] = 2
            valid = True
            for v in adj[u]:
                if v != p and not dfs(v, u):
                    valid = False
                    break
            visited[u] = 3
            return valid

        adj = buildAdj()
        valid = dfs(0, 0)

        return len(visited) == n and valid
