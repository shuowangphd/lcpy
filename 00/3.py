class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = res = 0
        for j,ele in enumerate(s):
            if ele in d and i <= d[ele]:
                i = d[ele]+1
            else:
                res = max(res, j-i+1)
            d[ele] = j
        return res