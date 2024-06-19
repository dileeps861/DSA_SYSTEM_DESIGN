from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        
        pacific = deque()
        atlantic = deque()
        
        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))
        for j in range(n):
            pacific.append((0, j))
            atlantic.append((m - 1, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(queue):
            reachable = set()
            while queue:
                x, y = queue.popleft()
                reachable.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in reachable and heights[nx][ny] >= heights[x][y]:
                        queue.append((nx, ny))
            return reachable

        reachable_pacific = bfs(pacific)
        reachable_atlantic = bfs(atlantic)

        return list(reachable_pacific.intersection(reachable_atlantic))
