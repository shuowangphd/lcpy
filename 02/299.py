class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        res0 = sum([x==y for x,y in zip(secret, guess)])
        res1 = sum(min(secret.count(x), guess.count(x)) for x in set(guess))-res0
        return str(res0)+'A'+str(res1)+'B'