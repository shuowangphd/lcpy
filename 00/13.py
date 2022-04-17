class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        res, pre = -1000, 1000
        for i in s:
            cur = d[i]
            if pre < cur:
                res -= pre
            else:
                res += pre
            pre = cur
        return res+pre