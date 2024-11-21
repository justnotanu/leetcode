class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        g = [[0] * n for _ in range(m)]
        
        # Mark guards and walls in the grid
        for i, j in guards:
            g[i][j] = 2  # Mark guard position
        
        for i, j in walls:
            g[i][j] = 2  # Mark wall position
        
        # Directions for guard visibility (up, right, down, left)
        dirs = (-1, 0, 1, 0, -1)  # This allows us to loop through directions
        
        # Simulate guard coverage
        for i, j in guards:
            for a, b in pairwise(dirs):
                x, y = i, j
                while 0 <= x + a < m and 0 <= y + b < n and g[x + a][y + b] < 2:
                    x += a
                    y += b
                    g[x][y] = 1  # Mark as guarded
        
        # Count unguarded cells
        return sum(v == 0 for row in g for v in row)
