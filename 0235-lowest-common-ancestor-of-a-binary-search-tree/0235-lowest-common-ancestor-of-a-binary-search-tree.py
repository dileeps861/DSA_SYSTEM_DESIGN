# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if q.val < p.val:
            return self.lowestCommonAncestor(root, q, p)
        
        if root.val <= q.val and p.val <= root.val:
            return root
        elif root.val <= q.val and root.val <= p.val:
            return self.lowestCommonAncestor(root.right, q, p)
        else:
            return self.lowestCommonAncestor(root.left, q, p)
