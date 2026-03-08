class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = 0
        def valid(i,j):
            if j>len(s):
                return False
            if s[i:j] == s[i:j][::-1]:
                return True
            return False

        max_substring = 0
        start = 0
        while start < len(s):
            if valid(start, start+k):
                max_substring+=1
                start += k
            elif valid(start,start+k+1):
                max_substring+=1
                start+=(k+1)
            else:
                start+=1
        return max_substring
                
        