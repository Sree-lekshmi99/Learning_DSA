# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        num = []
        path = []
        def dfs(node):
            if not node:
                return 
            path.append(node.val)
            if not node.left and not node.right:
                num.append(path.copy())
            
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()
        
        dfs(root)
        con = [int(''.join(map(str,n)),2) for n in num]
        

        # print(num)/
        return sum(con)

        