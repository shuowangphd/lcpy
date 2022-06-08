class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def isPalindrome(l, r):
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            res = 2000
            for j in range(i, n):
                if (isPalindrome(i, j)):
                    res = min(res, dp(j+1) + 1)
            return res
        
        return dp(0) - 1