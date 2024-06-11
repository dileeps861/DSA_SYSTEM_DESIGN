# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = [True]
        def dfs(node):
            if not node:
                return 0
            leftD = dfs(node.left)
            rightD = dfs(node.right)
            diff = abs(leftD - rightD) <= 1
            ans[0] = diff and ans[0]
            return max(leftD, rightD) + 1
        dfs(root)
        return ans[0]
