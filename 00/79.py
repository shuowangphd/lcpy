class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(ind, i, j):
            if self.found: return
            if ind == k:
                self.found = True
                return 
            if i < 0 or i >= m or j < 0 or j >= n: return 
            c = board[i][j]
            if c != word[ind]: return
            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(ind + 1, i+x, j+y)
            board[i][j] = c
        self.found = False
        m, n, k = len(board), len(board[0]), len(word)
        for i, j in product(range(m), range(n)):
            if self.found: return True
            dfs(0, i, j)
        return self.found