# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
        inorder(root)

        def balance(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            arr[mid].left = balance(l,mid-1)
            arr[mid].right = balance(mid+1,r)
            return arr[mid]


        
        return balance(0, len(arr)-1)

        