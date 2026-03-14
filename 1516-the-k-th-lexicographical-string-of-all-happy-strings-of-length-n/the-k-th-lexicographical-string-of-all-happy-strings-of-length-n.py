class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        hs = []
        def rec(s):
            if len(s) == n:
                if 'aa' in s or 'bb' in s or 'cc' in s:
                    return
                hs.append(s)
                return
            rec(s+'a')
            rec(s+'b')
            rec(s+'c')
        rec('')
        if k > len(hs):
            return ''
        return hs[k-1]
        