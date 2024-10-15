class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        ans = 0     # Total number of swaps needed
        cnt = 0     # Count of black balls encountered

        # Traverse the string from left to right
        for i in range(n):
            if s[i] == '1':
                cnt += 1  # Increment count for each black ball
            else:
                ans += cnt  # Add count of black balls for each white ball

        return ans  # Return total swaps needed