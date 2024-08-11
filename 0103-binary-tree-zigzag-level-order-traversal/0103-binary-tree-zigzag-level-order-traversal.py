# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        level = 0
        while q:
            size = len(q)
            inr = []
            while size:
                node = q.popleft()
                inr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
            if level % 2 != 0:
                res.append(inr[::-1])
            else:
                res.append(inr)
            level += 1
        return res
