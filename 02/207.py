class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [[] for _ in range(numCourses)]
        oud = [0] *numCourses
        for p in prerequisites:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = deque()
        for i in range(numCourses):
            if oud[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            x = dq.popleft()
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        return k == numCourses