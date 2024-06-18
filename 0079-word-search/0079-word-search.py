class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0:
            return True if not word else False
        m = len(board[0])
        ans = [False]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, soFar):
            if soFar == word:
                ans[0] = True
                return
            if len(soFar) >= len(word):
                return  # Stop if the current path is longer than the word

            for u,v in dirs:
                k,l = i + u, j + v
                if k >= 0 and k < n and l >= 0 and l < m and board[k][l] != '*':
                    char = board[k][l]
                    board[k][l] = "*"
                    dfs(k,l, soFar + char)
                    board[k][l] = char
                    if ans[0]:  # Stop further recursion if word is found
                        return
        for i in range(n):
            for j in range(m):
                if board[i][j] == "*":
                    continue
                char = board[i][j]
                board[i][j] = "*"
                dfs(i,j, char)
                board[i][j] = char
                if ans[0]:
                    return True
        return False
