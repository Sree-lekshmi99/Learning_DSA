class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        length = 0
        for i, c in enumerate(s):
            if c == '*':
                if length > 0:
                    length -= 1
            elif c == '#':
                length *= 2
            elif c == '%':
                pass
            else:
                length += 1
            lengths[i] = length

        if k < 0 or k >= lengths[-1]:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            cur_len = lengths[i]
            if c == '*':
                continue  
            elif c == '#':
                half = cur_len // 2
                if k >= half:
                    k -= half  
            elif c == '%':
                k = cur_len - 1 - k  
            else:
                if k == cur_len - 1:
                    return c  
        return '.'
        