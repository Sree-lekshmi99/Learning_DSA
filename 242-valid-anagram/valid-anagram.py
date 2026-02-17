class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = Counter(s)
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char]-=1

        return True
        
        