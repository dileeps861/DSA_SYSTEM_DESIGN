class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0:
            return True if not word else False
        m = len(board[0])
        ans = [False]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, idx):
            if idx == len(word):
                ans[0] = True
                return

            for u, v in dirs:
                k, l = i + u, j + v
                if k >= 0 and k < n and l >= 0 and l < m and board[k][l] == word[idx]:
                    char = board[k][l]
                    board[k][l] = "*"
                    dfs(k, l, idx + 1)
                    board[k][l] = char
                    if ans[0]:  # Stop further recursion if word is found
                        return

        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue
                char = board[i][j]
                board[i][j] = "*"
                dfs(i, j, 1)
                board[i][j] = char
                if ans[0]:
                    return True
        return False
