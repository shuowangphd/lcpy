class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = len(nums)-1
        while l > 0 and nums[l-1] >= nums[l]:
            l -= 1
        if l == 0:
            nums.reverse()
            return 
        l -= 1
        while nums[r] <= nums[l]:
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1