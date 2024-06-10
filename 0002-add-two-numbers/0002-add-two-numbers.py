# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        head = l1
        carry = 0
        prev = None
        while l1 or l2:
            if(l1 and l2):
                total = l1.val + l2.val + carry
                l1.val, carry = total % 10, total // 10
                l1,l2,prev = l1.next, l2.next, l1
            elif not l2:
                total = l1.val + carry
                l1.val, carry = total % 10, total // 10
                l1, prev = l1.next, l1
            else:
                total = l2.val + carry
                l2.val, carry = total % 10, total // 10
                l2, prev.next,prev = l2.next,l2, l2
        if carry:
            prev.next = ListNode(carry)
        return head
