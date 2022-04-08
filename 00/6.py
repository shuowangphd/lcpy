class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        line = ['']*numRows
        i,j = 0,1
        for x in s:
            line[i]+=x
            if i == 0:
                j = 1
            elif i == numRows-1:
                j = -1
            i += j
        return ''.join(line)