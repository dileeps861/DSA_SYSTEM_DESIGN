# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def dfs(i, min_val, max_val):
            # Base case: if index is out of bounds or current value out of valid range
            if i >= n or not (min_val < preorder[i] < max_val):
                return (None, i)

            # Create the current node
            node = TreeNode(preorder[i])
            # Recursively build the left subtree
            nodeLeft, i = dfs(i + 1, min_val, node.val)
            # Recursively build the right subtree
            nodeRight, i = dfs(i, node.val, max_val)
            # Set left and right children
            node.left = nodeLeft
            node.right = nodeRight
            return (node, i)

        # Initial call with the full range of valid values
        root, _ = dfs(0, float('-inf'), float('inf'))
        return root
