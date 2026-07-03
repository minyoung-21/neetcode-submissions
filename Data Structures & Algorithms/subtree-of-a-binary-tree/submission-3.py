# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            if self.isSubtreeHelper(root, subRoot):
                return True
            else:
                # we need to rethink about this here
                # we need to check until root reaches the last leaf
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            # there is either 
            # 1. both missing
            # 2. one of them missing
            if not subRoot:
                return True
            
        return False
    
    def isSubtreeHelper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root and subRoot:
            # print(root.val, subRoot.val)
            if root.val == subRoot.val:
                # check left and right
                return self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)
            else:
                # need a way to break out of it
                return False
        else:
            # need a way to break out of it
            if not root and not subRoot:
                return True
            return False