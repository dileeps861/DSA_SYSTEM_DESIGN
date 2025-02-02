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

        carry = 0
        head = None
        node = None
        while l1 or l2:
            sum = carry
            temp = None
            if l1:
                sum += l1.val
                temp = l1
                l1 = l1.next
            if l2:
                sum += l2.val
                temp = l2
                l2 = l2.next
            temp.val = sum % 10
            carry = sum // 10
            if not head:
                head = temp
            else:
                node.next = temp
            node = temp
        if carry > 0:
            node.next = ListNode(carry)
        return head
