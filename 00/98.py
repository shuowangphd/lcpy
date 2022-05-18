# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(nd,l,r):
            if not nd:
                return True
            ndv = nd.val
            if ndv <= l or ndv >= r:
                return False
            return dfs(nd.left,l,ndv) and dfs(nd.right,ndv,r)
        return dfs(root,-inf,inf)