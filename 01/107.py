# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res