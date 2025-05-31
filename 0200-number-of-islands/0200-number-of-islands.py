class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])
        num_of_islands = 0

        def is_a_valid_move(i, j):
            return i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == "1"

        def find_connected_lands(i, j):
            grid[i][j] = "2"
            for dir_i, dir_j in dirs:
                new_i, new_j = i + dir_i, j + dir_j
                if is_a_valid_move(new_i, new_j):
                    find_connected_lands(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # do something recusrively to find connected land
                    find_connected_lands(i, j)
                    num_of_islands += 1

        return num_of_islands
