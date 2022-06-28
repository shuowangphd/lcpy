class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob1(nums):
            a,b = 0,0
            for i in nums:
                a,b = b, max(a+i,b)
            return b
        return max(rob1(nums[:-1]),rob1(nums[1:]))