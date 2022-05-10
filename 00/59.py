class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        xi,yi,dx,dy = 0,0,1,0
        for i in range(1,n*n+1):
            res[yi][xi]=i
            if not 0 <= yi+dy < n or not 0 <= xi+dx < n or res[yi+dy][xi+dx]:
                dy,dx = dx,-dy
            yi,xi = yi+dy,xi+dx
        return res