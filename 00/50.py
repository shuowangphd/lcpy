class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1/x
            n = -n
        while(n):
            if n&1:
                res *= x
                n -= 1
            else:
                n >>= 1
                x = x*x
        return res