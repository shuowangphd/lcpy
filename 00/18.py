class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j >i+1 and nums[j]==nums[j-1]:
                    continue
                l, r = j + 1, n - 1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return res