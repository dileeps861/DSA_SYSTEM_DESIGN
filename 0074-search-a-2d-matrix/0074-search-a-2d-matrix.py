class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                # regular binary search
                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    midI = left + (right - left) // 2
                    if matrix[mid][midI] == target:
                        return True
                    elif matrix[mid][midI] < target:
                        left = midI + 1
                    else:
                        right = midI - 1
                break

            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
