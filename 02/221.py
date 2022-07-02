class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, res = len(matrix), len(matrix[0]), 0
        dp, onesRow, onesCol = ([[0]*(n+1) for i in range(m+1)] for cnt in range(3))

        for i, j in product(range(m-1, -1, -1), range(n-1, -1, -1)):
            onesRow[i][j] = 1 + onesRow[i][j+1] if matrix[i][j] == '1' else 0
            onesCol[i][j] = 1 + onesCol[i+1][j] if matrix[i][j] == '1' else 0
            
        for i, j in product(range(m-1, -1, -1), range(n-1, -1, -1)):
            dp[i][j] = min(onesRow[i][j], onesCol[i][j], dp[i+1][j+1]+1) if matrix[i][j] == '1' else 0
            res = max(res, dp[i][j])
        return res**2