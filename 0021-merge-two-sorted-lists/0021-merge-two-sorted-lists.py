# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        node = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    node = head
                else:
                    node.next = list1
                    node = node.next
                list1 = list1.next 
            else:
                if not head:
                    head = list2
                    node = head
                else:
                    node.next = list2
                    node = node.next

                list2 = list2.next
            
            
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return head