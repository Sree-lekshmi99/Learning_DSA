class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        flag = False
        while n>1:
            mid = 2**(n-1)
            if k == mid:
                return '0' if flag else '1'
            elif k>mid:
                k = 2**n - k
                flag = not flag
            n-=1
        return '1' if flag else '0'
        