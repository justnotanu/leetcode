from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Create a DP array initialized to 0
        dp = [[0] * n for _ in range(m)]
        total_squares = 0
        
        # Fill the DP array
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # First row or first column
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    total_squares += dp[i][j]
        
        return total_squares       