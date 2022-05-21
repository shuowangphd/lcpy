class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns,nt = len(s)+1,len(t)+1
        dp = [[0]*ns for _ in range(nt)]
        for x in range(ns):
            dp[0][x] = 1
        for x in range(1, ns):
            for y in range(1, nt):
                if s[x - 1] == t[y - 1]:
                    dp[y][x] = dp[y - 1][x - 1] + dp[y][x - 1]
                else:
                    dp[y][x] = dp[y][x - 1]
        return dp[-1][-1]