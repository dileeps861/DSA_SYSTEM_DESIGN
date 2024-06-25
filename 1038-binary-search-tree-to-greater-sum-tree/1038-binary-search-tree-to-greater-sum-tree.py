# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def bstSum(node, sum):
            if not node:
                return sum
            sum = bstSum(node.right, sum)
            node.val += sum
            return bstSum(node.left, node.val)
        bstSum(root, 0)
        return root