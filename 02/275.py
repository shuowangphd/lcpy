class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n =len(citations)
        l,r = 0,n-1
        while l <= r:
            i = (l+r)//2
            if citations[i] == n-i:
                return n-i
            elif citations[i] > n-i:
                r = i-1
            else:
                l = i+1
        return n-l