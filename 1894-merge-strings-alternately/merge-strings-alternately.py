class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = 0
        n = 0
        ans = []
        while m <= len(word1)-1 and n<= len(word2)-1:
            ans.append(word1[m])
            ans.append(word2[n])
            m+=1
            n+=1
        if len(word1)>len(word2):
            while m<=len(word1)-1:
                ans.append(word1[m])
                m+=1

        else:
            while n<=len(word2)-1:
                ans.append(word2[n])
                n+=1
        return ''.join(ans)
        