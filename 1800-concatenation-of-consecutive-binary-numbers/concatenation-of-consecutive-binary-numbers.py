class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9 + 7
        for i in range(1,n+1):
            bits = len(bin(i)) -2
            ans = ((ans<<bits)+i)%MOD
        # string = ''.join(stack)
        return ans
        # return int(string) if int(string)<