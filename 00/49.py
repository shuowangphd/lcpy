class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = ''.join(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()