# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we need to check at every node
        # so we use helper

        if p and q:
            return self.isSameTreeHelper(p, q)
        if p and not q or q and not p:
            return False
        
        return True
    def isSameTreeHelper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val == q.val:
                # continue checking
                return self.isSameTreeHelper(p.left, q.left) and self.isSameTreeHelper(p.right, q.right)
            else:
                return False
        else:
            if not p and not q:
                return True
            return False