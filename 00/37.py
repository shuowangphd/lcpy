class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[True]*9 for i in range(9)]        
        col = [[True]*9 for i in range(9)]
        sub = [[True]*9 for i in range(9)]
        to_add = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = int(board[i][j]) - 1
                    row[i][d] = col[j][d] = sub[i//3*3+j//3][d] = False
                else:
                    to_add.append((i, j))

        def backtrack():
            if not to_add: 
                return True
            i, j = to_add.pop()
            for d in range(9):
                if row[i][d] and col[j][d] and sub[i//3*3+j//3][d]:
                    board[i][j] = str(d+1)
                    row[i][d] = col[j][d] = sub[i//3*3+j//3][d] = False
                    if backtrack():
                        return True
                    board[i][j] = '.'
                    row[i][d] = col[j][d] = sub[i//3*3+j//3][d] = True
            to_add.append((i, j))
            return False

        backtrack()