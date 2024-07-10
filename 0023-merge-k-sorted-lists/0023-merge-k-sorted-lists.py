# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        prev = head
        pq = []
        count = 0
        for index, ls in enumerate(lists):
            if ls:
                tup = (ls.val, count, ls)
                count += 1
                heappush(pq, tup)
        while pq:
            count += 1
            val, _, node = heappop(pq)
            prev.next = node
            if node.next:
                heappush(pq, (node.next.val, count, node.next))
            prev = node

        return head.next
