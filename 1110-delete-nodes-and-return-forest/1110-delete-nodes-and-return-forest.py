# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        del_set = set(to_delete)

        res = []

        def dfs(node):
            if node is None:
                return node

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in del_set:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node

        root = dfs(root)
        if root:
            res.append(root)
        return res
