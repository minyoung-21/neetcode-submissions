"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        first_node = Node(node.val,[])
        ht = {node:first_node}

        def dfs(original_node: Optional['Node']) -> Optional['Node']:
            # do sth
            for neighbor in original_node.neighbors:
                if neighbor not in ht:
                    new_node = Node(neighbor.val, [])
                    ht[neighbor] = new_node
                    dfs(neighbor)
                ht[original_node].neighbors.append(ht[neighbor])
            
            return ht[original_node]

        return dfs(node)