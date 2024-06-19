class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(set)

        for u, v in prerequisites:
            adj[v].add(u)

        visited = dict()
        ans = [True]
        stack = []
        def dfs(u):
            if u in visited:
                if visited[u] == 1:
                    ans[0] = False
                return
            visited[u] = 1
            for v in adj[u]:
                if v not in visited or visited[v] == 1:
                    dfs(v)

            visited[u] = 2
            stack.append(u)

        for u in range(numCourses):
            if u not in visited:
                dfs(u)
            if not ans[0]:
                break
        if not ans[0]:
            return []
        return stack[::-1]
