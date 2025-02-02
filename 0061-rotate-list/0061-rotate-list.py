# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # First pass: find the length and the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Find the new tail: (length - k - 1) steps from the head
        newTail = head
        for i in range(length - k - 1):
            newTail = newTail.next

        newHead = newTail.next
        newTail.next = None  # Break the list

        # Attach the old tail to the old head
        tail.next = head
        return newHead
