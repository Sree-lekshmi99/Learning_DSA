class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        letter = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        
        l = 0
        r = len(lower)-1
        while l <r:
            if not lower[l].isalnum():
                l+=1
                continue
            if not lower[r].isalnum():
                r-=1
                continue
            elif lower[l]!=lower[r]:
                return False
            l+=1
            r-=1
                
        return True

        