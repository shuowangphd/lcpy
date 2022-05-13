class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        l,r = 1, min(x,2**16)
        mid = (l+r)//2
        while mid > l:
            mid2 = mid**2
            if mid2 == x:
                return mid
            if mid2 > x:
                r = mid
            else:
                l = mid
            mid = (l+r)//2
        return l