class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums = list(range(1, n+1))
        res = ''
        k -= 1
        n2 = math.factorial(n)
        while n > 0:
            n2 /= n
            n -= 1
            i = int(k//n2)
            k = k%n2
            res += str(nums[i])
            nums.pop(i)
        return res