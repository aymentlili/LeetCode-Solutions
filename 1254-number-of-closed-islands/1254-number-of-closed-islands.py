class Solution(object):
    def closedIsland(self, grid):
        n = len(grid)
        m = len(grid[0])
        closed_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    is_closed = True
                    queue = [(i, j)]
                    grid[i][j] = 1  
                    while queue:
                        r, c = queue.pop()
                        if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                            is_closed = False
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                                grid[nr][nc] = 1  
                                queue.append((nr, nc))
                    if is_closed:
                        closed_islands += 1
        return closed_islands