class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def isValidMove(i, j, board):
            # Check column
            for k in range(i):
                if board[k][j] == "Q":
                    return False

            # Check for main diagonal
            k, m = i - 1, j - 1
            while k >= 0 and m >= 0:
                if board[k][m] == "Q":
                    return False
                k -= 1
                m -= 1

            # Check for anti-diagonal
            k, m = i - 1, j + 1
            while k >= 0 and m < n:
                if board[k][m] == "Q":
                    return False
                k -= 1
                m += 1

            return True

        res = []

        def dfs(row, grid):
            if row == n:
                res.append(["".join(row) for row in grid])
                return

            for j in range(n):
                if isValidMove(row, j, grid):
                    grid[row][j] = "Q"
                    dfs(row + 1, grid)
                    grid[row][j] = "."

        dfs(0, [["."] * n for _ in range(n)])
        return res
