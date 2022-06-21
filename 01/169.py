class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num,cnt = 0,0
        for i in nums:
            if not cnt:
                num,cnt = i,1
            elif num == i:
                cnt += 1
            else:
                cnt -= 1
        return num