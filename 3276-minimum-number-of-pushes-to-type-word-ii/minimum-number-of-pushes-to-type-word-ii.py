class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sortedFreq = sorted(counts.values(), reverse = True)
        res = 0

        for i, freq in enumerate(sortedFreq):
            res += ((i // 8) + 1) * freq
        return res