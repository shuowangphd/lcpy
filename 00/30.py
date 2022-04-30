class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or words==[]:
            return []
        ns=len(s)
        nword=len(words[0])
        nsub=len(words)*nword
        times={}
        for word in words:
            if word in times:
                times[word]+=1
            else:
                times[word]=1
        res=[]
        for i in range(min(nword,ns-nsub+1)):
            self.findAnswer(i,ns,nword,nsub,s,times,res)
        return res
    def findAnswer(self,strstart,ns,nword,nsub,s,times,res):
        wordstart=strstart
        curr={}
        while strstart+nsub<=ns:
            word=s[wordstart:wordstart+nword]
            wordstart+=nword
            if word not in times:
                strstart=wordstart
                curr.clear()
            else:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+nword]]-=1
                    strstart+=nword
                if wordstart-strstart==nsub:
                    res.append(strstart)