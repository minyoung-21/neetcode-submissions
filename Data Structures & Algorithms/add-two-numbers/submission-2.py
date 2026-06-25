# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        res = ListNode(-1)
        copy = res

        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + carry
                if value >= 10:
                    carry = 1
                else:
                    carry = 0
                res.next = ListNode(value % 10)
            else:
                if l1:
                    value = l1.val + carry
                    if value >= 10:
                        carry = 1
                    else:
                        carry = 0
                    res.next = ListNode(value % 10)

                if l2:
                    value = l2.val + carry
                    if value >= 10:
                        carry = 1
                    else:
                        carry = 0
                    res.next = ListNode(value % 10)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            res.next = ListNode(carry)
        return copy.next
                