class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while r < m and c >= 0:
            num = matrix[r][c]
            if target == num: 
                return True
            if target > num:
                r += 1
            else:
                c -= 1
        return False