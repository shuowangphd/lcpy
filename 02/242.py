class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dp = [0]*26
        for i in s:
            dp[ord(i)-ord('a')] += 1
        for i in t:
            ind = ord(i)-ord('a')
            if not dp[ind]: return False
            dp[ind] -= 1
        return True