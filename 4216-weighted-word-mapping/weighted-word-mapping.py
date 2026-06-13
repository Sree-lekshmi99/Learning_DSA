class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # precompute: each letter -> its weight % 26
        letter_weight = {chr(97 + i): weights[i] for i in range(26)}
        
        ans = []
        for word in words:
            res = sum(letter_weight[ch] for ch in word) % 26
            ans.append(chr(ord('z') - res))
        
        return "".join(ans)