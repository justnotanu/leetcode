class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Sort robots by their positions
        robot.sort()
        # Sort factories by their positions
        factory.sort(key=lambda x: x[0])
        
        n = len(robot)
        m = len(factory)
        
        # Create a DP table with (n+1) x (m+1) initialized to infinity
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots require 0 distance
        dp[0][0] = 0
        
        # Fill the DP table
        for j in range(1, m + 1):
            position, limit = factory[j - 1]
            for i in range(n + 1):
                # If we don't use this factory at all
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
                
                # Try to assign robots to this factory
                total_distance = 0
                for k in range(1, limit + 1):
                    if i - k < 0:
                        break
                    total_distance += abs(robot[i - k] - position)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)
        
        return dp[n][m]

