class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m1 = [1]*m
        for _ in range(n-1):
            for i in range(1,m):
                m1[i] += m1[i-1] 
        return m1[-1]