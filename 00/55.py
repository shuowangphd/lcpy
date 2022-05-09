class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i,ni in enumerate(nums):
            if i > r:
                return False
            r = max(i+ni,r)
        return True