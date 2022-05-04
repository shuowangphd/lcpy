class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(target, index, path):
            if target < 0:
                return 1
            if target == 0:
                res.append(path)
                return 0
            for i in range(index, len(candidates)):
                if dfs(target-candidates[i], i, path+[candidates[i]]):
                    break
        dfs(target, 0, [])
        return res