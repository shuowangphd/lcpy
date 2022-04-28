class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        l, r, res = n, n, []
        self.dfs(l,r, res, "")
        return res
    def dfs(self, l,r, res, s):
        if not l and not r:
            res.append(s)
            return
        if l:
            self.dfs(l-1, r, res, s + "(")
        if r and r>l:
            self.dfs(l, r-1, res, s + ")")