# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = ListNode(67)
        curr = head
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        while node1 is not None or node2 is not None:
            
            if node1.val > node2.val:
                curr.next = ListNode(node2.val)
                curr = curr.next
                if node2.next is None:
                    curr.next = node1
                    return head.next
                node2 = node2.next
            else:
                curr.next = ListNode(node1.val)
                curr = curr.next
                if node1.next is None:
                    curr.next = node2
                    return head.next
                node1 = node1.next
        
        