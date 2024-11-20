class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                oneCount = 0
                zerosCount = 0
                for u, v in dirs:
                    # print(i, j, i+u, j+v)
                    if 0 <= u + i < m and 0 <= v + j < n:
                        if board[u + i ][v + j] == 0 or board[u + i ][v + j] == 2:
                            zerosCount += 1
                        elif board[u + i ][v + j] == 1 or board[u + i ][v + j] == -1:
                            oneCount += 1
                # print(i,j, zerosCount, oneCount)
                if board[i][j] == 1 and oneCount > 3:
                    board[i][j] = -1
                elif board[i][j] == 0 and oneCount == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and oneCount < 2:
                    board[i][j] = -1
        # print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
