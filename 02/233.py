class Solution:
    def countDigitOne(self, n: int) -> int:
        q, res, x = n, 0, 1
        while q:
            digit = q % 10
            q = q//10
            res += q * x
            if digit == 1:
                res += n % x + 1
            elif digit > 1:
                res += x
            x *= 10
        return res