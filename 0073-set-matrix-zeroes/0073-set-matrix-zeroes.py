class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Use the first row and column to mark zeroes
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    # Determine if the first row or first column should be zero
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set matrix elements to zero based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set the first row and column to zero if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
