class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Fill DP table from right to left
        for col in range(n - 2, -1, -1):  # Start from second last column
            for row in range(m):
                # Check possible moves downwards
                if row + 1 < m and grid[row + 1][col + 1] > grid[row][col]:
                    dp[row][col] = max(dp[row][col], dp[row + 1][col + 1] + 1)
                # Check possible moves straight
                if grid[row][col + 1] > grid[row][col]:
                    dp[row][col] = max(dp[row][col], dp[row][col + 1] + 1)
                # Check possible moves upwards
                if row - 1 >= 0 and grid[row - 1][col + 1] > grid[row][col]:
                    dp[row][col] = max(dp[row][col], dp[row - 1][col + 1] + 1)

        # Find maximum moves starting from any cell in the first column
        max_moves = max(dp[i][0] for i in range(m))
        
        return max_moves

    