class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [0]+[2e4]*(n-1)
        for mi in range(m):
            dp[0] += grid[mi][0]
            for ni in range(1,n):
                dp[ni] = grid[mi][ni]+min(dp[ni],dp[ni-1])
        return dp[-1]