"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def __init__(self):
        self.visited = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node in self.visited:
            return self.visited[node]
        if not node:
            return node
        nodeClone = Node(node.val)
        if not node.neighbors:
            return nodeClone
        nodeClone.neighbors = []
        self.visited[node] = nodeClone
       
        for child in node.neighbors:
            nodeClone.neighbors.append(self.cloneGraph(child))
        return nodeClone