# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if node:
                depth = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
            return depth
        return dfs(root, 0)