class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk, res = [(")", -1)], 0
        for i in range(len(s)):
            if s[i] == ")" and stk[-1][0] == "(":
                stk.pop()
                res = max(res, i-stk[-1][1])
            else:
                stk.append((s[i], i))
        return res