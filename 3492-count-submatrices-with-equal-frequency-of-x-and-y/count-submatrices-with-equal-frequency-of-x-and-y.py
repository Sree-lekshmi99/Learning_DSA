class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        prefix_x = [0] * len(grid[0])
        prefix_y = [0] * len(grid[0])

        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        for r in range(rows):
            nr = 0
            nc = 0 
            for c in range(cols):
                if grid[r][c] == 'X':
                    nr+=1
                if grid[r][c]=='Y':
                    nc+=1
                prefix_x[c]+= nr
                prefix_y[c]+=nc
                if prefix_y[c]>0 and prefix_y[c] == prefix_x[c]:
                    ans+=1
        return ans

        