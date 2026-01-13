class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key= len)
        for i,ch in enumerate(shortest_word):
            for s in strs:
                if s[i] != ch:
                    return shortest_word[:i]
        return shortest_word
        