class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count_fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    count_fresh += 1
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        res = -1
        while q:
            sz = len(q)
            print(q)
            while sz > 0:
                i, j = q.popleft()
                for u, v in dirs:
                    k, l = u + i, v + j
                    if (
                        k >= 0
                        and k < len(grid)
                        and l >= 0
                        and l < len(grid[k])
                        and grid[k][l] == 1
                    ):
                        count_fresh -= 1
                        q.append((k, l))
                        grid[k][l] = 2
                sz -= 1
            res += 1
        if count_fresh > 0:
            return -1
        return res
