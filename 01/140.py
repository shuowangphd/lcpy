class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s, wordDict, memo):
            if s in memo: return memo[s]
            if not s: return []
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    resultOfTheRest = helper(s[len(word):], wordDict, memo)
                    for item in resultOfTheRest:
                        item = word + ' ' + item
                        res.append(item)
            memo[s] = res
            return res
        return helper(s, wordDict, {})