class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)
    def getSum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s
    def getSumRange(self, left, right): 
        return self.getSum(right) - self.getSum(left - 1)
    def addValue(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & (-idx)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(len(nums))
        for i, v in enumerate(nums):
            self.bit.addValue(i+1, v)
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.bit.addValue(index+1, diff)
        self.nums[index] = val
    def sumRange(self, left: int, right: int) -> int:
        return self.bit.getSumRange(left+1, right+1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)