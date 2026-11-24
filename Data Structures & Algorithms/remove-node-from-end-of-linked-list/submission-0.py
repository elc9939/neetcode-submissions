# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ctr = 0
        h = head
        while h:
            h = h.next
            ctr += 1
        s = ListNode()
        h = s
        h.next= head
        for i in range(ctr-n):
            h = h.next
        h.next = h.next.next
        return s.next
