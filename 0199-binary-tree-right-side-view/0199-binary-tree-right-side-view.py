# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque([root])
        res = []
        if not root:
            return res
        while q:
            sz = len(q)
            while sz:
                popped = q.popleft()
                if sz == 1:
                    res.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                sz -= 1
        return res
