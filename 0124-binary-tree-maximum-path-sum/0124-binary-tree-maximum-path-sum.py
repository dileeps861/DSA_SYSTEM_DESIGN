# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(node):

            if not node:
                return 0

            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))
            res[0] = max(res[0], leftMax + rightMax + node.val)
            return max(leftMax + node.val, rightMax + node.val)
        dfs(root)
        return res[0]
        