from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        cellSet = defaultdict(set)

        for i in range(len(board)):
            column = set()
            for j in range(len(board[i])):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rowSet[j]:
                    
                    return False
                rowSet[j].add(val)
                if val in column:
                    
                    return False
                column.add(val)

                # now add cell
                # i + 1 // 3 
                cellNum = (i // 3) * 3 + (j // 3)
                if val in cellSet[cellNum]:
                    return False
                cellSet[cellNum].add(val)
        return True