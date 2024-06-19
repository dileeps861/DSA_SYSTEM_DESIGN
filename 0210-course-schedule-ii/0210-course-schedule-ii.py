from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[v].append(u)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        ans = [True]
        stack = []

        def dfs(u):
            if visited[u] == 1:  # Cycle detected
                ans[0] = False
                return
            if visited[u] == 2:  # Already fully processed
                return
            visited[u] = 1  # Mark as visiting
            for v in adj[u]:
                if visited[v] != 2:  # Only visit if not fully processed
                    dfs(v)
                    if not ans[0]:  # Early stop if cycle detected
                        return
            visited[u] = 2  # Mark as fully processed
            stack.append(u)

        for u in range(numCourses):
            if visited[u] == 0:
                dfs(u)
            if not ans[0]:  # Early stop if cycle detected
                break
        
        if not ans[0]:
            return []
        
        return stack[::-1]

