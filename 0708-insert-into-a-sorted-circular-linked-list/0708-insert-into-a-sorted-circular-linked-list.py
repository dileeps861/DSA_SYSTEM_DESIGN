"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        prev = head
        node = head.next
        prevPrev = None
        while True:
            if prev.val <= insertVal <= node.val:
                newNode = Node(insertVal, node)
                prev.next = newNode

                return head

            prev, node, prevPrev = node, node.next, prev
            if prev == head:
                break
        if prev == head:
            while True:
                if prevPrev.val >= prev.val <= node.val:
                    newNode = Node(insertVal, prev)
                    prevPrev.next = newNode
                    return head
                prevPrev, prev, node = prev, node, node.next
        return head
