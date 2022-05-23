class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        pre = prices[0]
        for p in prices:
            res += max(0,p-pre)
            pre = p
        return res