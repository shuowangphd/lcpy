class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        if len(p) - p.count('*') > ns:
            return False
        dp = [True] + [False]*ns
        for i in p:
            if i != '*':
                for di in range(ns-1,-1,-1):
                    dp[di+1] = dp[di] and (i == s[di] or i == '?')
                dp[0] = False
            else:
                for di in range(ns):
                    dp[di+1] = dp[di+1] or dp[di]
        return dp[-1]