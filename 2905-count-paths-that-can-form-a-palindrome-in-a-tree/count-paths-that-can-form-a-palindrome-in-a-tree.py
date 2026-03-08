class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        from collections import defaultdict

class Solution:
    def countPalindromePaths(self, parent, s):
        n = len(parent)
        g = [[] for _ in range(n)]
        
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1   # mask of root before starting

        def dfs(u, mask):
            nonlocal ans

            for v in g[u]:
                new_mask = mask ^ (1 << (ord(s[v]) - ord('a')))

                # same mask => all counts even
                ans += cnt[new_mask]

                # differ by one bit => exactly one odd count
                for b in range(26):
                    ans += cnt[new_mask ^ (1 << b)]

                cnt[new_mask] += 1
                dfs(v, new_mask)

        dfs(0, 0)
        return ans