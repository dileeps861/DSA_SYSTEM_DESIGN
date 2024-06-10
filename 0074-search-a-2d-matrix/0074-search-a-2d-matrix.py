class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = m -1

        while i <= j:
            k = 0
            l = n - 1
            mid = i + (j - i) // 2
            leftVal = matrix[mid][k]
            rightVal = matrix[mid][l]
            if leftVal <= target and rightVal >= target:

                while k <= l:
                    midInner = k + (l - k) // 2
                    val = matrix[mid][midInner]
                    if val == target:
                        return True
                    if val < target:
                        k = midInner + 1
                    else:
                        l = midInner - 1
            if leftVal > target:
                j = mid - 1
            else:
                i = mid + 1
        return False