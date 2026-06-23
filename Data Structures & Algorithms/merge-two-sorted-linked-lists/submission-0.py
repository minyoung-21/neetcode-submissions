# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        res = ListNode()

        temp = res
        i = 0

        while p1 and p2:
            if p1.val > p2.val:
                res.next = ListNode(p2.val)
                p2 = p2.next
            elif p1.val < p2.val:
                res.next = ListNode(p1.val)
                p1 = p1.next
            else:
                # p1 and p2 are the same val
                res.next = ListNode(p1.val)
                res = res.next
                res.next = ListNode(p2.val)

                p1 = p1.next
                p2 = p2.next
            res = res.next
        
        if p1:
            res.next = p1
        if p2:
            res.next = p2
        return temp.next