# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if q.val < p.val:
            p, q = q, p
        while root:
            if root.val <= q.val and p.val <= root.val:
                return root
            elif root.val <= q.val and root.val <= p.val:
                root = root.right
            else:
                root = root.left
        return root
