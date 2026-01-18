class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c = 0
        v = 'aeiou'
        a = 0
        for ch in s:
            if ch.isalpha():
                if ch not in v:
                    c+=1
                else:
                    a+=1
        # if c>0:
        #     print(a//c)
        

        return a//c if c>0 else 0
        