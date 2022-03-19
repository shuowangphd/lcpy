class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,ele in enumerate(nums):
            if ele in d:
                return [d[ele],i]
            d[target-ele]=i
