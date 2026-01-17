class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        if s == "" and t:
            return True
        if s and t == "":
            return False
        if s =="" and t == "":
            return True
        while l<len(s) and r<len(t):
            if s[l] == t[r]:
                l+=1
                r+=1
            else:
                r+=1
            
            if l == len(s):
                return True
            
        return False

        