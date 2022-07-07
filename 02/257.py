# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(nd, s):
            if not nd: return
            if not s: 
                s = str(nd.val)
            else:
                s += "->"+str(nd.val)
            if not nd.left and not nd.right:
                res.append(s)
            dfs(nd.left,s)
            dfs(nd.right,s)
        dfs(root,"")
        return res