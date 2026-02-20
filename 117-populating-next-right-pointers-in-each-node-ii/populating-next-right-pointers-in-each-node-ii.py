"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque()
        q.append([root,0])
        prev_vl = 0
        prev_node = None
        while q:
            node,vl = q.popleft()
            if prev_vl and prev_vl == vl:
                prev_node.next = node
            prev_node = node
            prev_vl = vl

            if node.left:
                q.append([node.left,vl+1])
            if node.right:
                q.append([node.right,vl+1])
        return root
        