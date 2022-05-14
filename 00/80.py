class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in nums:
            if l < 2 or i != nums[l-2]:
                nums[l] = i
                l += 1
        return l