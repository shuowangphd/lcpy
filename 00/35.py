class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid+1
            else:
                r = mid
        return l