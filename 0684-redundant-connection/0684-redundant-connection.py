from typing import List
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = defaultdict(int)  # 0 = unvisited, 1 = visiting, 2 = visited
        parent = {}
        cycle = []

        def dfs(node, par):
            visited[node] = 1
            parent[node] = par
            for neighbor in adj[node]:
                if neighbor == par:
                    continue
                if visited[neighbor] == 0:
                    if dfs(neighbor, node):
                        return True
                elif visited[neighbor] == 1:
                    # Cycle detected, record the cycle path
                    cycle.append((node, neighbor))
                    current = node
                    while current != neighbor:
                        cycle.append((current, parent[current]))
                        current = parent[current]
                    return True
            visited[node] = 2
            return False

        for u in adj:
            if visited[u] == 0:
                if dfs(u, -1):
                    break

        # Iterate from the end of the edges list to find the redundant edge
        cycle_set = set(cycle)
        for u, v in reversed(edges):
            if (u, v) in cycle_set or (v, u) in cycle_set:
                return [u, v]

        return []
        