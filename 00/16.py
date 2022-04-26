class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while l < r:
                s3 = nums[i] + nums[l] + nums[r]
                if s3 == target:
                    return s3
                if abs(s3 - target) < abs(res - target):
                    res = s3
                if s3 < target:
                    l += 1
                elif s3 > target:
                    r -= 1
        return res