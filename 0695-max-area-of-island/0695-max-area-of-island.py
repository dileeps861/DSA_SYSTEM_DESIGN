class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        DIRS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q = deque([(i, j)])
                    count = 0
                    while q:
                        k, l = q.pop()
                        count += 1
                        for u, v in DIRS:
                            m, n = k + u, l + v
                            if (
                                m >= 0
                                and m < len(grid)
                                and n >= 0
                                and n < len(grid[m])
                                and grid[m][n] == 1
                            ):
                                q.append((m, n))
                                grid[m][n] = 0
                    res = max(res, count)
        return res