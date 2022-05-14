class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n-1
        mid = r//2
        while l <= r:
            mv = matrix[mid//n][mid%n]
            if mv == target:
                return True
            if mv < target:
                l = mid+1
            else: 
                r = mid-1
            mid = (r+l)//2
        return False