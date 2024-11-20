# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import defaultdict

        columns = defaultdict(list)

        def dfs(node: TreeNode, col: int, row: int, idx: int) -> None:
            if not node:
                return

            # Add current node with its row number and index
            columns[col].append((row, idx, node.val))

            # Use idx to maintain left to right order
            dfs(node.left, col - 1, row + 1, idx)
            dfs(node.right, col + 1, row + 1, idx + 1)

        # Perform DFS traversal
        dfs(root, 0, 0, 0)

        # Find the range of columns
        min_col = min(columns.keys())
        max_col = max(columns.keys())

        # Build result by sorting each column's values
        result = []
        for col in range(min_col, max_col + 1):
            # Sort by row first, then by index, then by value
            sorted_col = [
                val
                for row, idx, val in sorted(
                    columns[col], key=lambda x: (x[0], x[1])
                )
            ]
            result.append(sorted_col)

        return result
