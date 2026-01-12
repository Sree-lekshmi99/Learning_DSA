class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        i = 0
        while i <len(points)-1:
            x1 =  abs(points[i][0] - points[i+1][0])
            x2 =  abs(points[i][1] - points[i+1][1])
            i+=1
            m = max(x1,x2)
            ans +=m
        return ans

        