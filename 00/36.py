class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if (i,cur) in s or (cur,j) in s or (i//3,j//3,cur) in s:
                    return False
                s.add((i,cur))
                s.add((cur,j))
                s.add((i//3,j//3,cur))
        return True