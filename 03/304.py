class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ny,nx = len(matrix), len(matrix[0])
        self.m = [ [0 for j in range(nx+1)] for i in range(ny+1) ]
        for yi in range(ny):
            for xi in range(nx):
                self.m[yi+1][xi+1] = self.m[yi][xi+1]+self.m[yi+1][xi]-self.m[yi][xi]+matrix[yi][xi]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.m[row2+1][col2+1]+self.m[row1][col1]-self.m[row2+1][col1]-self.m[row1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)