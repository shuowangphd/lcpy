class Solution:
    def addDigits(self, num: int) -> int:
        if not num//10:
            return num
        return (num-1)%9+1