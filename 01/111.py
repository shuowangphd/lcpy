# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        dl = self.minDepth(root.left)
        dr = self.minDepth(root.right)
        if not dl or not dr: return dl+dr+1
        return 1+min(dl,dr)