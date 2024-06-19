class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        q = deque()

        def add_to_queue(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'P'
                q.append((i, j))

        for i in range(m):
            add_to_queue(i, 0)
            add_to_queue(i, n - 1)
        for j in range(n):
            add_to_queue(0, j)
            add_to_queue(m - 1, j)

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = 'P'
                    q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'P':
                    board[i][j] = 'O'