# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = head
        r = head

        while r and r.next:

            l = l.next
            r = r.next.next
        
        # r is at the end
        # l is in the mid

        l1 = head
        l2 = l.next
        l.next = None
        curr = 0
        prev = None

        while l2:
            curr = l2
            l2 = l2.next
            curr.next = prev
            prev = curr
        print(curr)

        l2 = curr
        while l2:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1
            
            l1 = t1
            l2 = t2
            
        