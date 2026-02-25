# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        def dfs(node,path):
            nonlocal total_sum
            if not node:
                return 0
            
            if not node.left and not node.right:
                total_sum += path*10 + node.val
            dfs(node.left, path*10+node.val)
            dfs(node.right, path*10+node.val)
           
        dfs(root,0)
        return total_sum

        