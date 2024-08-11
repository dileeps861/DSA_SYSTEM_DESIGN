# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, mn, mx):
            if node is None:
                return True

            if mn >= node.val or mx <= node.val:
                return False
            return validate(node.left, mn, node.val) and validate(
                node.right, node.val, mx
            )

        return validate(root, float("-inf"), float("inf"))
