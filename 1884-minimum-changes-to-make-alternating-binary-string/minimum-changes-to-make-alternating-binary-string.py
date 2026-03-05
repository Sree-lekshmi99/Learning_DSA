class Solution:
    def minOperations(self, s: str) -> int:
        A = 0 
        B = 0  

        for i, ch in enumerate(s):
            expA = '0' if i % 2 == 0 else '1'
            if ch != expA:
                A += 1
            else:
                B += 1
        return min(A, B)