class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = collections.deque([[beginWord, 1]])
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    wd2 = word[:i] + c + word[i+1:]
                    if wd2 in wordList:
                        wordList.remove(wd2)
                        q.append([wd2, length + 1])
        return 0