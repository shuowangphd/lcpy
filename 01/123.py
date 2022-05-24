class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = b2 =  1e5
        p1 = p2 = 0
        for p in prices:
            b1 = min(b1,p)
            p1 = max(p1,p - b1)
            b2 = min(b2,p - p1)
            p2 = max(p2,p - b2)
        return p2