class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(s[i])
            elif s[i] == "*":
                if res:
                    res.pop()
                else:
                    continue
            elif s[i]== "#":
                res.extend(res)
            else:
                res.reverse()
        return ''.join(res)
        