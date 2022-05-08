class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def dfs(queens, qdif, qsum):
            p = len(queens)
            if p == n:
                self.res += 1
                return
            for q in range(n):
                if q not in queens and p-q not in qdif and p+q not in qsum: 
                    dfs(queens+[q], qdif+[p-q], qsum+[p+q])  
        dfs([],[],[])
        return self.res