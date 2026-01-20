class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # k = 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        # if k == len(needle):
        return -1
                
                        
        