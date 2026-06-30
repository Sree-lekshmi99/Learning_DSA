class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # r = 0
        l = 0
        ans = 0
        count = {'a':0, 'b':0, 'c':0}
        for r in range(len(s)):
            count[s[r]] +=1
            while all(count.values()):
                ans+=len(s)-r
                count[s[l]] -=1
                l+=1
        return ans
                


        