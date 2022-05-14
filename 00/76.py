class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = collections.Counter(t)
        l0,r0,l,cnt = 0,-1,0,len(t)
        for r,c in enumerate(s):
            if c in d: 
                cnt -= d[c]>0
                d[c] -= 1
            while not cnt:
                if r0 < 0 or r-l <r0-l0:
                    r0,l0 = r,l
                if s[l] in d:
                    d[s[l]] += 1
                    cnt += d[s[l]]>0
                l += 1
        return s[l0:r0+1]