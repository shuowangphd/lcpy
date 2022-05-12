class Solution:
    def isNumber(self, s: str) -> bool:
        dot = e = dig = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if dot or e: return False
                dot = True
            elif char in ['e','E']:
                if e or not dig:
                    return False
                e, dig = True, False
            elif char.isdigit():
                dig = True
            else:
                return False
        return dig