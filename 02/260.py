class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1, x2 = 0, 0
        for n in nums:
            x1 ^= n
        for bit in range(32):
            if x1 & 1 << bit:
                i = bit
                break
        for n in nums:
            if n & 1 << i:
                x2 ^= n
        return [x1 ^ x2, x2]