class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k >= n / 2:
            return sum(i - j  for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            localMax = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(dp[i-1][j-1]+profit, dp[i-1][j-1], localMax[j-1]+profit)
                dp[i][j] = max(dp[i][j - 1], localMax[j])
        return dp[k][-1]