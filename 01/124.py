# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1000
        def dfs(nd):
            nonlocal res
            if not nd: return 0
            vl = dfs(nd.left)
            vr = dfs(nd.right)
            res = max(res,vl+nd.val+vr)
            return max(vl+nd.val,vr+nd.val,nd.val,0)
        dfs(root)
        return res