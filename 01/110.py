# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(nd):
            if not nd: return 0
            hl = height(nd.left)
            hr = height(nd.right)
            dh = abs(hl-hr)
            if hl < 0 or hr < 0 or dh > 1:
                return -1
            return max(hl,hr)+1
        ht = height(root)
        return ht > -1