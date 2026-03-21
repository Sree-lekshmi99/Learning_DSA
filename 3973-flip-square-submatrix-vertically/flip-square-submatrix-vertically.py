class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        # def flipper():

        # rows =  len(grid)
        # cols = len(grid[0])

        # topleft = grid[x][y]
        # bottomleft = grid[x+k-1][y]
        # topright = grid[x][y+k-1]
        # bottomright = grid[x+k-1][y+k-1]

        top = x
        bottom = x + k
        while top < bottom:
            for col in range(y, y+k):
                grid[top][col],grid[bottom-1][col] = grid[bottom-1][col], grid[top][col]
            top+=1
            bottom-=1
        return grid








        