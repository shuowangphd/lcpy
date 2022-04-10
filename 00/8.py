class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == '':
            return 0
        sign = [1,-1] [s[0] == '-']
        res = i0 = 0
        if sign == -1 or s[0]== '+':
            i0 = 1
        for i in range(i0,len(s),1):
            if s[i].isdigit():
                res = res*10+ord(s[i])-ord('0')
            else:
                break
        return min(2**31-1, max(sign*res,-2**31))