# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast and slow pointers
        # give an heads up of n+1 to fast pointer
        fast = head
        count = 0
        while fast and count <= n:
            fast = fast.next
            count += 1
        slow = head
        if not fast and count <= n:
            return head.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
