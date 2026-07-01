# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return l + r
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l, r = 0, 0

        if root.left:
            l = self.maxDepth(root.left)
        if root.right:
            r = self.maxDepth(root.right)

        print(l, r)
        return 1 + max(l, r)
        

    # def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> int:

    #     # get the biggest from l and r and traverse after + 1
    #     # do res = l + r 
    #     # return the max(res, l + r)
    #     l, r = 0, 0
    #     if root.left and root.right:
    #         temp = max(self.diameterOfBinaryTreeHelper(root.left), self.diameterOfBinaryTreeHelper(root.right))
    #         l = temp + 1
    #         r = temp + 1
    #     elif root.left and not root.right:
    #         # only left node exists
    #         l = 1 + self.diameterOfBinaryTreeHelper(root.left)
    #     elif root.right and not root.left:
    #         r = 1 + self.diameterOfBinaryTreeHelper(root.right)
        
    #     print(l, r)
    #     return l + r