class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ny,nx = len(board),len(board[0])
        dp = [[0]*(nx+2) for i in range(ny+2)]
        for yi in range(ny):
            for xi in range(nx):
                if board[yi][xi] == 1:
                    for i in range(3):
                        for j in range(3):
                            dp[yi+i][xi+j] += 1
                    dp[yi+1][xi+1] -= 1
        for yi in range(ny):
            for xi in range(nx):
                cnt = dp[yi+1][xi+1]
                if cnt < 2 or cnt > 3:
                    board[yi][xi] = 0
                elif cnt == 3:
                    board[yi][xi] = 1