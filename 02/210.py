class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [set() for _ in range(numCourses)]
        outdegree = [[] for _ in range(numCourses)]
        for p0,p1 in prerequisites:
            indegree[p0].add(p1)
            outdegree[p1].append(p0)
        res, start = [], [i for i in range(numCourses) if not indegree[i]]
        while start:
            newStart = [] 
            for i in start:
                res.append(i)
                for j in outdegree[i]:
                    indegree[j].remove(i)
                    if not indegree[j]:
                        newStart.append(j)
            start = newStart
        return res if len(res) == numCourses else []