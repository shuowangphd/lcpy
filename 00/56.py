class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        l,r = intervals[0]
        for i in intervals:
            if i[0]>r:
                res.append([l,r])
                l,r = i
            else:
                r = max(r,i[1])
        res.append([l,r])
        return res