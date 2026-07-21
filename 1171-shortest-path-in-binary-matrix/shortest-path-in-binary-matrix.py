class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0],[1, 1]]
        q = deque([(0,0,1)])
        visited = set((0,0))
        if grid[0][0] == 1 or grid[rows-1][rows-1] == 1:
            return -1
        
        while q:
            r,c,path = q.popleft()
            if (r,c) == (rows-1,rows-1):
                return path
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == 0:
                    q.append([nr,nc,path+1])
                    visited.add((nr,nc))
        return -1
                    
                
                

            






        return bfs(0,0)  
        