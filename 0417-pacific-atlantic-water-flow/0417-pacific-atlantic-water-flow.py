class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        qP = deque()
        qA = deque()

        m = len(heights)
        if m == 0 or len(heights[0]) == 0:
            return []
        n = len(heights[0])
        for i in range(n):
            qP.append((0, i))
            qA.append((m - 1, i))
        for j in range(m):
            qP.append((j, 0))
            qA.append((j, n - 1))

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def movable(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True

        def bfs(q):
            reachable = set()

            while q:
                i, j = q.popleft()
                reachable.add((i, j))
                for u, v in dirs:
                    k, l = i + u, j + v
                    if not movable(k, l):
                        continue
                    if (k, l) in reachable:
                        continue
                    if heights[k][l] >= heights[i][j]:
                        q.append((k, l))
            return reachable

        reachableP = bfs(qP)
        reachableA = bfs(qA)

        return reachableA.intersection(reachableP)
