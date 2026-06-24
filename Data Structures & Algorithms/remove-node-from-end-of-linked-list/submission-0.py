# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = 0

        i = 0

        while i < n and fast:
            fast = fast.next
            i += 1

        while fast and slow:
            
            prev = slow
            fast = fast.next
            slow = slow.next
        
        print(slow)
        print(prev)

        if prev and slow and slow.next:
            prev.next = slow.next
        elif prev and not slow.next:
            prev.next = None
        elif not prev and slow.next:
            head = slow.next
        else:
            return None
        
        return head