class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nm = [len(matrix[0]),len(matrix)-1]
        res = []
        dire,yi,xi = 0,0,-1
        while nm[dire%2]:
            for i in range(nm[dire%2]):
                if dire%2:
                    yi += 2-dire
                else:
                    xi +=1-dire
                res.append(matrix[yi][xi])
            nm[dire%2] -= 1
            dire = (dire+1)%4
        return res