class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        while r > l:
            if height[l] < height[r]:
                h = height[l]
                res = max(res, (r-l)*h)
                while r > l and height[l] <= h:
                    l += 1
            else:
                h = height[r]
                res = max(res, (r-l)*h)
                while r > l and height[r] <= h:
                    r -= 1            
        return res