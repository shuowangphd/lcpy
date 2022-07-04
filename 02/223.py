class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        res = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        x1 = max(ax1,bx1)
        x2 = min(ax2,bx2)
        y1 = max(ay1,by1)
        y2 = min(ay2,by2)
        if x1 < x2 and y1 < y2:
            res += (x2-x1)*(y1-y2)
        return res