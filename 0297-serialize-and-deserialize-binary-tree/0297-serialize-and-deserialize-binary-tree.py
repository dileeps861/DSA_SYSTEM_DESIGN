# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # root then  (left--)(right)
        if root is None:
            return '(None)'
        
        res = '(' + str(root.val)
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        res += ')'
        return res
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        globalIdx = [0]

        def isLeaf(dataS):
            if dataS[globalIdx[0]: globalIdx[0] + 6] == '(None)':
                globalIdx[0] += 6
                return True
            return False
        
        def dfs(dataS):
            if isLeaf(dataS):
                return None

            num = ''
            if dataS[globalIdx[0]] == '(':
                globalIdx[0] += 1
            if dataS[globalIdx[0]] == '-':
                num = '-'
                globalIdx[0] += 1
            while globalIdx[0] < len(dataS):
                digi = dataS[globalIdx[0]]
                if not digi.isnumeric():
                    break
                num += digi
                globalIdx[0] += 1
            val = int(num)
            node = TreeNode(val)
            node.left = dfs(dataS)
            node.right = dfs(dataS)
            if dataS[globalIdx[0]] == ')':
                globalIdx[0] += 1
            return node

        return dfs(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))