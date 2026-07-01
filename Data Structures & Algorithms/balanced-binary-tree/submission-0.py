# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.b = True
        if not root:
            return True
        
        # if abs(r - l) > 1:
        #     return False
        self.height(root)

        return self.b
    
    def height(self, root: Optional[TreeNode]) -> int:
        l, r = 0, 0

        if root.left:
            l = 1 + self.height(root.left)
        if root.right:
            r = 1 + self.height(root.right)
        
        if abs(l-r) > 1:
            self.b = False
        
        return max(l, r)
        