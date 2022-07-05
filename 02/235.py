# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv,qv = p.val, q.val
        if pv > qv:
            pv,qv = qv,pv
        while root:
            rv = root.val
            if rv >= pv and rv <= qv: return root
            if rv < pv: root = root.right
            else: root = root.left