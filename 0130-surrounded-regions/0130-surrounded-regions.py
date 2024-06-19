class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        q = deque()
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "P"
                q.append((i, 0))
            if board[i][n - 1] == "O":
                board[i][n - 1] = "P"
                q.append((i, n - 1))
        for i in range(n):
            if board[0][i] == "O":
                board[0][i] = "P"
                q.append((0, i))
            if board[m - 1][i] == "O":
                board[m - 1][i] = "P"
                q.append((m - 1, i))
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O":
                    board[nx][ny] = "P"
                    q.append((nx, ny))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "P":
                    board[i][j] = "O"

