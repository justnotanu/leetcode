import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions for moving in the grid
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Min-heap priority queue
        min_heap = [(0, 0, 0)]  # (obstacles removed, x, y)
        # Visited array to track the minimum obstacles removed to reach each cell
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0
        
        while min_heap:
            obstacles_removed, x, y = heapq.heappop(min_heap)
            
            # If we reached the bottom-right corner
            if x == m - 1 and y == n - 1:
                return obstacles_removed
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    new_obstacles_removed = obstacles_removed + grid[nx][ny]
                    
                    # Only proceed if we found a better way to reach (nx, ny)
                    if new_obstacles_removed < visited[nx][ny]:
                        visited[nx][ny] = new_obstacles_removed
                        heapq.heappush(min_heap, (new_obstacles_removed, nx, ny))
        
        return -1  # If there's no valid path
    