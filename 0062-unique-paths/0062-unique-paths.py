class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None] * n for _ in range(m)]

        def findPath(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if dp[i][j] is not None:
                return dp[i][j]
            sum = 0
            if i + 1 < m:
                sum += findPath(i + 1, j)
            if j + 1 < n:
                sum += findPath(i, j + 1)
            dp[i][j] = sum
            return sum

        return findPath(0, 0)
