class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt,p,i0, n = 0,1,0, len(nums)
        for i in range(n):
            if not nums[i]:
                cnt += 1
                i0 = i
            else: p *= nums[i]
        res = [0]*n
        if cnt == 1:
            res[i0] = p
        elif not cnt:
            for i in range(n):
                res[i] = p//nums[i]
        return res