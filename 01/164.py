class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mi, n = min(nums), len(nums)
        mai = max(nums)-mi
        if not mai: return 0
        bucketSize = math.ceil(mai/ (n - 1))
        minBucket = [2e9] * n
        maxBucket = [-1] * n
        for x in nums:
            idx = (x - mi) // bucketSize
            minBucket[idx] = min(minBucket[idx], x)
            maxBucket[idx] = max(maxBucket[idx], x)
        res = bucketSize
        prev = maxBucket[0]
        for i in range(1, n):
            if minBucket[i] == 2e9: continue
            res = max(res, minBucket[i] - prev)
            prev = maxBucket[i]
        return res