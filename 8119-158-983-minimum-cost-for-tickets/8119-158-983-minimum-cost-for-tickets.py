class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)  # dp[i] will hold the min cost for covering days up to days[i-1]

        for i in range(1, n + 1):
            # Start with the cost of a 1-day pass
            dp[i] = dp[i - 1] + costs[0]
            
            # Check for a 7-day pass
            j = i - 1
            while j >= 0 and days[j] > days[i - 1] - 7:
                j -= 1
            dp[i] = min(dp[i], dp[j + 1] + costs[1])
            
            # Check for a 30-day pass
            j = i - 1
            while j >= 0 and days[j] > days[i - 1] - 30:
                j -= 1
            dp[i] = min(dp[i], dp[j + 1] + costs[2])

        return dp[n]
