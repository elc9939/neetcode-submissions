# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            prev = None
            while head:
                head.next, prev, head = prev, head, head.next
            return prev
        
        
        slow = head
        fast = head
        ctr = 0
        while fast.next != None:
            fast = fast.next
            if ctr%2: slow = slow.next
            ctr += 1
        second = slow.next
        slow.next = None      # cut the first half off
        a = reverseList(second)
        b = head

        #
        for i in range(ctr):
            if (i+1)%2:
                temp = b.next
                b.next = a
                b = temp
            else:
                temp = a.next
                a.next = b
                a = temp