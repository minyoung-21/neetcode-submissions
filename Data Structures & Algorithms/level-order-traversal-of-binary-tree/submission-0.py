# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # hint: use a breadth first search

        res = []
        if not root:
            return res
        q = [root]
        # we need to get each node's left and right
        l = 0
        while q:
            l = len(q)
            sub_arr = []
            
            for i in range(l):
                node = q.pop(0)
                sub_arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(sub_arr)
            

        return res
