# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        msf = -10001
        self.count = 0
        # maybe preorder?
        # nope it should be just depth first search
        # track which is better
        self.dfs(root, msf)
        # print(msf, self.count)
        return self.count
    
    def dfs(self, node: TreeNode, max_so_far: int):
        if node:
            # print(node.val)
            
            if node.val >= max_so_far:
                # max changed
                max_so_far = max(max_so_far, node.val)
                self.count += 1
            self.dfs(node.left, max_so_far)
            self.dfs(node.right, max_so_far)