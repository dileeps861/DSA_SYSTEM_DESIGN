class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[-1, -1], [0, -1], [1, -1]]
        res = 0
        dp = [0] * rows

        for col in range(1, cols):
            dpcp = [0] * rows
            found = 0
            for row in range(rows):
                for dr, dc in dirs:
                    u, v = row + dr, col + dc
                    if 0 <= u < rows and 0 <= v < cols and grid[row][col] > grid[u][v]:
                        if col > 1 and dp[u] == 0:
                            continue
                        dpcp[row] = max(dpcp[row], dp[u] + 1)
                res = max(res, dpcp[row])
                if dpcp[row] > 0:
                    found += 1
            if found == 0:
                break
            dp = dpcp
            # print(dp)

        return res
