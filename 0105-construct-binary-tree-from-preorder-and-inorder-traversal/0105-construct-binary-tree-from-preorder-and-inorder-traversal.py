# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # low high, global preI
        # First make left sub tree before moving right
        globalI = [0]
        
        # Create a hash map for inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def findIdx(num, low, high):
            return inorder_map[num]
                    
        def construct(low, high):
            if low > high:
                return None
            num = preorder[globalI[0]]
            idx = findIdx(preorder[globalI[0]], low, high)
            node = TreeNode(num)
            globalI[0] += 1
            node.left = construct(low, idx - 1)
            node.right = construct(idx + 1, high)
            return node
        return construct(0, len(inorder) - 1)