class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        non_dupe = set()

        l = 0
        min_length = 0 
        for r in range(len(s)):
            while s[r] in non_dupe:
                non_dupe.remove(s[l])
                l+=1
            non_dupe.add(s[r])
            min_length = max(min_length ,r-l+1)
        return min_length
            

        