# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def iot(root, res):
            if root:
                iot(root.left,res)
                res.append(root.val)
                iot(root.right,res)
        res = []
        iot(root,res)
        return res