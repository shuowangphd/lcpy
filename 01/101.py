# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isS(nd1,nd2):
            if not nd1 and not nd2: return True
            if nd1 and nd2 and nd1.val == nd2.val: 
                return isS(nd1.left,nd2.right) and isS(nd1.right,nd2.left)
            return False
        return isS(root.left,root.right)