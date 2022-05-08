class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, qdif, qsum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in qdif and p+q not in qsum: 
                    dfs(queens+[q], qdif+[p-q], qsum+[p+q])  
        res = []
        dfs([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]