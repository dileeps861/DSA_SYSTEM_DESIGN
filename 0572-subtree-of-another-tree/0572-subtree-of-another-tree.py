# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            return False
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        ans = False
        if root.val == subRoot.val:
                ans = isSame(root, subRoot)
        if ans:
            return True
        ans = ans or self.isSubtree(root.left, subRoot) 
        if ans:
            return True
        return self.isSubtree(root.right, subRoot)
