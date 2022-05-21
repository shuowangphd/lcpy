# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        nd = root
        while nd:
            if nd.right: stack.append(nd.right)
            if nd.left: 
                nd.right = nd.left
                nd.left = None
            elif stack:
                nd.right = stack.pop()
            nd = nd.right