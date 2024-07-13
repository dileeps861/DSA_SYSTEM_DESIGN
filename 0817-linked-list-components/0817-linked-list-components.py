# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        st = set(nums)
        if len(st) <= 1:
            return len(st)
        node = head
        res = 1
        prev = None
        while node:
            if not st:
                break
            if node.val not in st:
                if prev:
                    res += 1
                prev = None
            elif node.val in st:
                prev = node
                st.remove(node.val)
            node = node.next
        return res
