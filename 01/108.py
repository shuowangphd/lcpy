# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n: return None
        return TreeNode(val = nums[n//2],left=self.sortedArrayToBST(nums[:n//2]),right=self.sortedArrayToBST(nums[n//2+1:]))