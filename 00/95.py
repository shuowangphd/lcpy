# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(l, r):
            if l > r: return [None]
            if l == r: return [TreeNode(l)]
            res = []
            for root in range(l, r+1):
                lns = dfs(l, root - 1)
                rns = dfs(root+1, r)
                for ln in lns:
                    for rn in rns:
                        rootNode = TreeNode(root, ln, rn)
                        res.append(rootNode)
            return res
        return dfs(1, n)