class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh= 0
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        minutes = 0
        directions= [(0,1),(1,0),(0,-1),(-1,0)]
        time = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh+=1
                if grid[row][col] == 2:
                    q.append((row,col))
        
       
        
        while q and fresh>0:
            # time+=1
            rotten_this_minute = False
            level = len(q)
            for i in range(len(q)):
                row , col = q.popleft()
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        fresh-=1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                    rotten_this_minute = True
            if rotten_this_minute:
                time+=1
        
                
        return time if fresh == 0 else -1
                        




        