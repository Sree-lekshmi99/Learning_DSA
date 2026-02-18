class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for y in strs:
            word = list(y)
            word.sort()
            word = ''.join(word)
            anagram_dict[word].append(y)
        print(anagram_dict)
        ans = []
        for key, val in anagram_dict.items():
            ans.append(val)
        return ans       