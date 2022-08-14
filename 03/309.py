class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, cool, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, cash, cool = max(hold, cash - p), max(cash, cool), hold + p
        return max(cash, cool)