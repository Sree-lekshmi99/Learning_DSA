class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        n = len(robot)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for pos, limit in factory:
            for i in range(n, 0, -1):
                dist = 0
                for k in range(1, limit + 1):
                    if i - k < 0:
                        break
                    dist += abs(robot[i - k] - pos)
                    if dp[i - k] != float('inf'):
                        dp[i] = min(dp[i], dp[i - k] + dist)
                        
        return dp[n]