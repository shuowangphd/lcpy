class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        m = {}
        return self.dfs(expression, m)
        
    def dfs(self, input, m):
        if input in m:
            return m[input]
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[input] = res
        return res