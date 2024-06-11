# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def findMxDepth(node):
            if not node:
                return 0
            maxDia = 0
            depthLeft = findMxDepth(node.left)
            depthRight = findMxDepth(node.right)
            maxDia += (depthLeft + depthRight)
            ans[0] = max(ans[0], maxDia)
            return max(depthLeft, depthRight) + 1
        findMxDepth(root)
        return ans[0]