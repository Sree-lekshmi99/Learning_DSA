class Solution:
    def residuePrefixes(self, s: str) -> int:
        count = 0
        set_char = set()
        n = len(s)
        curr = 0
        print(count)
        print(set_char)
        for i in range(len(s)):
            if s[i] not in set_char:
                set_char.add(s[i])
                curr+=1
            if curr == (i+1)%3:
                    count+=1
        return count
                
            
        
        