class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res,ny,nx = 0,len(grid),len(grid[0])
        def land(yi,xi):
            if yi<0 or xi<0 or yi>=ny or xi >=nx or grid[yi][xi]=="0":
                return
            grid[yi][xi]="0"
            land(yi-1,xi)
            land(yi+1,xi)
            land(yi,xi-1)
            land(yi,xi+1)
        for yi in range(ny):
            for xi in range(nx):
                if grid[yi][xi]=="1":
                    res += 1
                    land(yi,xi)
        return res