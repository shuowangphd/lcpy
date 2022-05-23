class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        pb = prices[0]
        for p in prices:
            if p < pb:
                pb = p
            else:
                res = max(res,p-pb)
        return res