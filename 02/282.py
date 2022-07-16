class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(idx, path, value, last):            
            if idx == n and value == target:
                res.append(path)     
            for i in range(idx + 1, n + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != "0"):
                    if last is None :
                        dfs(i, num[idx: i], tmp, tmp)
                    else:
                        dfs(i, path + '+' + num[idx: i], value + tmp, tmp)
                        dfs(i, path + '-' + num[idx: i], value - tmp, -tmp)
                        dfs(i, path + '*' + num[idx: i], value - last + last*tmp, last*tmp) 
        res, n = [], len(num)
        dfs(0, "", 0, None)
        return res