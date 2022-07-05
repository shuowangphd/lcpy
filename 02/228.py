class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        def app(l,r):
            if r == l:
                res.append(str(l))
            else:
                res.append(str(l)+'->'+str(r))
        res,l = [],nums[0]
        r = l
        for i in range(1,len(nums)):
            num = nums[i]
            if num == r+1:
                r = num
                continue
            app(l,r)
            l = r = num
        app(l,r)
        return res