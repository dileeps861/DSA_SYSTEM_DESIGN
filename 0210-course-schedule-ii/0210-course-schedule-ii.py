from collections import defaultdict
from typing import List

class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     adj = defaultdict(list)

    #     for u, v in prerequisites:
    #         adj[v].append(u)

    #     visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
    #     ans = [True]
    #     stack = []

    #     def dfs(u):
    #         if visited[u] == 1:  # Cycle detected
    #             ans[0] = False
    #             return
    #         if visited[u] == 2:  # Already fully processed
    #             return
    #         visited[u] = 1  # Mark as visiting
    #         for v in adj[u]:
    #             if visited[v] != 2:  # Only visit if not fully processed
    #                 dfs(v)
    #                 if not ans[0]:  # Early stop if cycle detected
    #                     return
    #         visited[u] = 2  # Mark as fully processed
    #         stack.append(u)

    #     for u in range(numCourses):
    #         if visited[u] == 0:
    #             dfs(u)
    #         if not ans[0]:  # Early stop if cycle detected
    #             break
        
    #     if not ans[0]:
    #         return []
        
    #     return stack[::-1]

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for u, v in prerequisites:
            adj[v].append(u)
            in_degree[u] += 1

        # Queue of all nodes with in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If the number of courses in the result is less than numCourses, there is a cycle
        if len(result) == numCourses:
            return result
        else:
            return []