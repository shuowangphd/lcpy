class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s2=s.split()
        np,ns = len(pattern),len(s2)
        if np != ns:
            return False
        d, d2 = {}, {}
        for i in range(np):
            if pattern[i] in d:
                if d[pattern[i]] != s2[i]:
                    return False
            else:
                d[pattern[i]] = s2[i]
            if s2[i] in d2:
                if d2[s2[i]] != pattern[i]:
                    return False
            else:
                d2[s2[i]] = pattern[i]
        return True