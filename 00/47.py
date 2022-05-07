class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for ni in nums:
            res2 = []
            for l in res:
                for i in range(len(l)+1):
                    res2.append(l[:i]+[ni]+l[i:])
                    if i<len(l) and l[i]==ni: break
            res = res2
        return res