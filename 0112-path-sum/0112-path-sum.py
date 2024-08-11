# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = []
        stack.append((root, root.val))
        visited = set()
        while stack:
            popped, sm = stack.pop(-1)
            if popped.left is None and popped.right is None and sm == targetSum:
                return True
            visited.add(popped)
            if popped.left and popped.left not in visited:
                stack.append((popped.left, popped.left.val + sm))
            if popped.right and popped.right not in visited:
                stack.append((popped.right, popped.right.val + sm))
        return False
