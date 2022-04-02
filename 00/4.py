class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        if n%2:
            return self.kth(nums1,nums2,n//2)
        return (self.kth(nums1,nums2,n//2-1)+self.kth(nums1,nums2,n//2))/2
    def kth(self,a,b,k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia,ib = len(a)//2,len(b)//2
        va,vb = a[ia],b[ib]
        if ia+ib < k:
            if va < vb:
                return self.kth(a[ia+1:],b,k-ia-1)
            return self.kth(a,b[ib+1:],k-ib-1)
        elif va < vb:
            return self.kth(a,b[:ib],k)
        return self.kth(a[:ia],b,k)