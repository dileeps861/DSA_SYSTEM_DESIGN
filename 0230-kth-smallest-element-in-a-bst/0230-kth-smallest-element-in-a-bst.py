# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [-1]
        idx = [0]

        def dfs(node):
            if node is None:
                return
            if node.left:
                dfs(node.left)
            idx[0] += 1
            if idx[0] == k:
                res[0] = node.val
            dfs(node.right)

        dfs(root)
        return res[0]
