# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dictInorder = {}
        for idx, val in enumerate(inorder):
            dictInorder[val] = idx
        i = [0]

        def buildRoot(low, high):
            if low > high:
                return None

            val = preorder[i[0]]
            mid = dictInorder[val]
            node = TreeNode(val)
            i[0] += 1
            node.left = buildRoot(low, mid - 1)
            node.right = buildRoot(mid + 1, high)
            return node

        return buildRoot(0, len(inorder) - 1)
