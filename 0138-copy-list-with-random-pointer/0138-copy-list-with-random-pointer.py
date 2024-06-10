"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # interst new cloned nodes in bewtween nodes of original list, and later restore original list
        if not head:
            return head
        node = head
        while node:
            newNode = Node(node.val)
            newNode.next = node.next
            node.next = newNode
            node = newNode.next

        # change random pointers of new list to random new node
        node = head
        while node:
             # Could be the case that there is no random pointer
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # Restore original list and build random connection of new noded
        node = head
        newHead = head.next
        newNode = newHead
        while node:
            # make nodes point to correct node
            node.next = newNode.next
            if newNode.next:
                newNode.next = newNode.next.next
            # node.next = node.next.next
            
            # move to new next node
            node = node.next
            newNode = newNode.next
            
        return newHead
            