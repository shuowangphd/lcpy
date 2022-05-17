class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ns = len(s)
        if ns < 4 or ns > 12:
            return []
        res = []
        def dfs(i,j,ip):
            if ip and (int(ip[-1]) > 255 or (ip[-1][0]=='0' and len(ip[-1])>1)):
                return
            if i == ns and j == 4:
                res.append('.'.join(ip))
                return
            if i == ns or j == 4 or (ns-i > 3*(4-j)):
                return
            dfs(i+1,j+1,ip+[s[i]])
            if i+1 < ns: 
                dfs(i+2,j+1,ip+[s[i:i+2]])
                if i+2 < ns: dfs(i+3,j+1,ip+[s[i:i+3]])
        dfs(0,0,[])
        return res