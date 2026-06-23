# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        if head == None:
            return 
        else:
            curr = head

        while curr != None:
            
            q = curr.next
            curr.next = prev # break
            prev = curr
            curr = q

        return prev