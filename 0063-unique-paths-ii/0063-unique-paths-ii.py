class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0]]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = {}
        def is_valid_move(i, j):
            return 0 <= i < m and 0 <= j <n and obstacleGrid[i][j] == 0

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            # obstacleGrid[i][j] = 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = 0
            for u, v in dirs:
                new_i, new_j = i + u, j + v
                if is_valid_move(new_i, new_j):
                    # obstacleGrid[i][j] = 2
                    memo[(i, j)] += dfs(new_i, new_j)
                    # obstacleGrid[i][j] = 0
            return memo[(i, j)] 
        if obstacleGrid[0][0] == 0:
            return dfs(0, 0)
        return 0