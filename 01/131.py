class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                si = s[:i]
                if si == si[::-1]:
                    dfs(s[i:], path+[si])
        res = []
        dfs(s, [])
        return res