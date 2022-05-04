class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nn = len(nums)
        for i in range(nn):
            while nums[i] > 0 and nums[i] <= nn and nums[i] != nums[nums[i]-1]:
                ni = nums[i]
                nums[i],nums[ni-1] = nums[ni-1], nums[i]
        for i in range(nn):
            if nums[i]!= i+1:
                return i+1
        return nn+1