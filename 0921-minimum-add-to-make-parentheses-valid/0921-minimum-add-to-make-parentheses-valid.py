class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0  # Count of unmatched opening parentheses
        close_count = 0  # Count of unmatched closing parentheses

        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1  # Match with an opening parenthesis
                else:
                    close_count += 1  # Unmatched closing parenthesis

        # Total unmatched parentheses is the sum of unmatched opens and closes
        return open_count + close_count

# Example usage
solution = Solution()
s = "()))"
print(solution.minAddToMakeValid(s))  # Output: 2