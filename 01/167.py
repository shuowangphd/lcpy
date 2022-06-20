class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while(1):
            ad = numbers[l]+numbers[r]
            if ad == target:
                return [l+1,r+1]
            if ad > target:
                r -=1
            else:
                l +=1