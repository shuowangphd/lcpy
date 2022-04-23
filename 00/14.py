class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strMin = min(strs,key=len)
        for i, ch in enumerate(strMin):
            for stri in strs:
                if stri[i] != ch:
                    return strMin[:i]
        return strMin