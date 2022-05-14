class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                res.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return res
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1