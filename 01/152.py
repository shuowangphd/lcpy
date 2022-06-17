class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn, res = 1,1,-10
        for i in nums:     
            mx, mn =  max(i, mx*i, mn*i), min(i, mx*i, mn*i) 
            res = max(mx, res)
        return res