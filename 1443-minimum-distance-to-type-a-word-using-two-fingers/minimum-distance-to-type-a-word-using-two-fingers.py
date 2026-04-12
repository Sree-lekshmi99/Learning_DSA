class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == 26: 
                return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)
        
        
        dp = [float('inf')] * 27
        dp[26] = 0
        
        for i in range(n):
            cur = ord(word[i]) - ord('A')
            new_dp = [float('inf')] * 27
            
            for j in range(27):
                if dp[j] == float('inf'):
                    continue
                
                if i == 0:
                   
                    new_dp[j] = 0
                    continue
                
                prev = ord(word[i-1]) - ord('A')
                
               
                new_dp[j] = min(new_dp[j],
                                dp[j] + dist(prev, cur))
                
              
                new_dp[prev] = min(new_dp[prev],
                                   dp[j] + dist(j, cur))
            
            dp = new_dp
        
        return min(dp)