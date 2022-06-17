class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = 1
        for i in range(n):
            dic = {'i':1}
            same = 0
            xi,yi = points[i]
            for j in range(i+1, n):
                xj,yj = points[j]
                if xj == xi and yj == yi: 
                    same += 1
                    continue
                if xj == xi: slope = 'i'
                else:slope = (yi-yj) * 1.0 /(xi-xj)
                if slope not in dic: dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m