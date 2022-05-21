# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def path(nd, lst, target):
            if not nd: return
            lst.append(nd.val)
            target -= nd.val
            if not nd.left and not nd.right: 
                if not target:
                    res.append(lst.copy())
            else:
                path(nd.left, lst, target)
                path(nd.right, lst, target)
            lst.pop()
        path(root,[],targetSum)
        return res