class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        flattenedItems = []

        def traversAndAdd(start, stop, step, isRow, fixIdx):
            for idx in range(start, stop, step):
                if isRow:
                    flattenedItems.append(matrix[fixIdx][idx])
                else:
                    flattenedItems.append(matrix[idx][fixIdx])

        while left < right and top < bottom:

            # Fill top row
            traversAndAdd(left, right, 1, True, top)
            top += 1
            # Fill right column
            traversAndAdd(top, bottom, 1, False, right - 1)
            right -= 1

            # Case when ther is just left one row or one column then in that case we need 
            # to break To avoid considering same row and columns again
            if not left < right or not top < bottom:
                break
            # Fill bottom row
            traversAndAdd(right - 1, left - 1, -1, True, bottom - 1)
            bottom -= 1

            # Fill left column
            traversAndAdd(bottom - 1, top - 1, -1, False, left)
            left += 1
        return flattenedItems
