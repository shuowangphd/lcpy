class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, n = 0, len(nums)
        res = n+1
        for j in range(n):
            target -= nums[j]
            while target <= 0:
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (n+1)