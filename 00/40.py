class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(target, index, path):
            if target < 0:
                return 1
            if target == 0:
                res.append(path)
                return 0
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if dfs(target - candidates[i], i + 1, path + [candidates[i]]):
                    break               
        dfs(target, 0, [])
        return res