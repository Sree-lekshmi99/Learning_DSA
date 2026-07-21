

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        q = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while q:
            r, c, path = q.popleft()
            if (r, c) == (rows-1, cols-1):
                return path
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    q.append((nr, nc, path + 1))

        return -1