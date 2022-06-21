class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            res = res*26+ord(i)-ord('A')+1
        return res