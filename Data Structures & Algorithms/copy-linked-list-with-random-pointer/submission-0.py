"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        node = head
        ht = {}

        while node:
            ht[node] = Node(node.val)
            node = node.next

        print(ht)
        node = head

        while node:
            ht[node].next = ht.get(node.next)
            ht[node].random = ht.get(node.random)
            node = node.next
        return ht[head]