class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        noOfIslands = 0
        for i in range(n):
            m = len(grid[i])
            for j in range(m):
                if grid[i][j] == "1":
                    noOfIslands += 1
                    stack = []
                    stack.append((i, j))
                    while stack:
                        p, q = stack.pop(-1)
                        for r, s in dirs:
                            u, v = p + r, q + s
                            if 0 <= u < n and 0 <= v < m and grid[u][v] == "1":
                                grid[u][v] = "0"
                                stack.append((u, v))
        return noOfIslands