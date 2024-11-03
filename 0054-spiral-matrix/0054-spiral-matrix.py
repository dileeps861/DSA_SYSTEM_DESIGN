class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        flattenedItems = []
        while left < right and top < bottom:

            # Fill top row
            for idx in range(left, right):
                flattenedItems.append(matrix[top][idx])
            top += 1
            # Fill right column
            for idx in range(top, bottom):
                flattenedItems.append(matrix[idx][right - 1])
            right -= 1

            if not left < right or not top < bottom:
                break
            # Fill bottom row
            for idx in range(right - 1, left - 1, -1):
                flattenedItems.append(matrix[bottom - 1][idx])
            bottom -= 1

            # Fill left column
            for idx in range(bottom - 1, top - 1, -1):
                flattenedItems.append(matrix[idx][left])
            left += 1
        return flattenedItems
