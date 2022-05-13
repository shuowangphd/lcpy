class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai,bi,carry = len(a)-1,len(b)-1,0
        res = ''
        while ai >= 0 or bi >= 0 or carry:
            av = int(a[ai]) if ai >= 0 else 0
            bv = int(b[bi]) if bi >= 0 else 0
            sum3 = av+bv+carry
            res = str(sum3%2)+res
            carry = sum3//2
            ai,bi = ai-1,bi-1
        return res