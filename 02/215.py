class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        nl, nm = len(left), len(mid)
        if k <= nl:
            return self.findKthLargest(left, k)
        elif k > nl + nm:
            return self.findKthLargest(right, k - nl - nm)
        else:
            return mid[0]