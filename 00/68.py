class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, nl = [], [], 0
        for w in words:
            if nl + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - nl):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, nl = [], 0
            cur += [w]
            nl += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]