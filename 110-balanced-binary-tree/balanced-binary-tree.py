# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
        
            leftn= dfs(root.left)
            rightn= dfs(root.right)
            if leftn == -1 or rightn == -1:
                return -1
            if abs(leftn - rightn) >1 :
                return -1
            return 1 + max(leftn,rightn)
        return dfs(root)!=-1