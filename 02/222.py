# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(root):
            if not root:
                return 0
            return 1 + getDepth(root.left)
        if not root:
            return 0
        l = getDepth(root.left)
        r = getDepth(root.right)
        if l == r:
            return pow(2, l) + self.countNodes(root.right)
        else:
            return pow(2, r) + self.countNodes(root.left)