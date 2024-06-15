# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse inorder and then return the count, if count becomes k that is the answer
        ans = [-1]
        def dfs(node, num):
            if not node:
                return num
            count = dfs(node.left, num)
            if count == k - 1 and ans[0] == -1:
                ans[0] = node.val
                return 0
            
            count = dfs(node.right, count + 1)
            if count == k and ans[0] == -1:
                ans[0] = node.val
                return 0
            return count
        dfs(root, 0)
        return ans[0]