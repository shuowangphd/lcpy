class Solution:
    def trap(self, height: List[int]) -> int:
        res,pre,l,r = 0,0,0,len(height)-1
        while l <= r:
            h = min(height[l],height[r])
            if h>pre:
                res += (h-pre)*(r-l+1)
                pre=h
            if h == height[l]:
                res -= height[l]
                l += 1
            else:
                res -= height[r]
                r -= 1
        return res