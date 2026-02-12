class Solution:
    def longestBalanced(self, s: str) -> int:
        # count =  counter(s)
        ans = 0
        n = len(s)
        for l in range(len(s)):
            count = defaultdict(int)
            for r in range(l , n):
                count[s[r]]+=1
                if len(set(count.values())) == 1:
                    ans = max(ans, r-l+1)
        return ans


        