# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        rev, res, level = False, [], [root]
        while level:
            clv,nextl = [],[]
            for nd in level:
                clv.append(nd.val)
                if nd.left:
                    nextl.append(nd.left)
                if nd.right:
                    nextl.append(nd.right)
            if rev:
                res.append(clv[::-1])
                rev = False
            else:
                res.append(clv)
                rev = True
            level = nextl
        return res   