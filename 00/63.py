class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [1]+[0]*(n-1)
        for mi in range(m):
            for ni in range(n):
                if obstacleGrid[mi][ni] == 1:
                    dp[ni] = 0
                elif ni > 0:
                    dp[ni] += dp[ni-1]
        return dp[-1]