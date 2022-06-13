# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stk = [], [root]
        while stk:
            nd = stk.pop()
            if nd:
                res.append(nd.val)
                stk.append(nd.right)
                stk.append(nd.left)
        return res