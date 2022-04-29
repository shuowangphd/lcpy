class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nh,nn = len(haystack), len(needle)
        for i in range(nh-nn+1):
            if haystack[i:i+nn] == needle:
                return i
        return -1