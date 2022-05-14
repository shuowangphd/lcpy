class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,l,r = 0,0,len(nums)-1
        while i <= r:
            if nums[i] == 0:
                nums[l],nums[i] = nums[i],nums[l]
                i,l= i+1,l+1
            elif nums[i] == 1:
                i += 1
            else:
                nums[r],nums[i] = nums[i],nums[r]
                r -= 1