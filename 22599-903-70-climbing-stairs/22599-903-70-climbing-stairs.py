class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Create a DP array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 1
        dp[2] = 2
        
        # Fill the DP array using the established relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
