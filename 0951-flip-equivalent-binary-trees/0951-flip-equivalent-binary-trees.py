# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # the way to do it is level order traversal and then sort the lists
        # if at any point we can not find equal sorted we dont have have equi bt
        # This approach is flawed bcs of the case when on path is in left and on the other tree on right
        # making level oreder taversal seem ok but in correct
        # using dfs, by comapring flip pair

        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        return root1.val == root2.val and ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))
