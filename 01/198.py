class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b = 0,0
        for i in nums:
            a,b = b, max(a+i,b)
        return b