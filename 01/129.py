# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(nd, su):
            nonlocal res
            su = su*10+nd.val
            if not nd.left and not nd.right:
                res += su
            else:
                if nd.left: dfs(nd.left, su)
                if nd.right: dfs(nd.right, su)
        dfs(root,0)
        return res