class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(nums, k, n, path):
            if k < 0 or n < 0:
                return 
            if k == 0 and n == 0:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]])
        res = []
        dfs(list(range(1, 10)), k, n, [])
        return res