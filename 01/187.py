class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        dict = defaultdict(int)
        for i in range(len(s)-9):
            seq = s[i:i+10]
            dict[seq] += 1
            if dict[seq] == 2:
                res.append(seq)
        return res