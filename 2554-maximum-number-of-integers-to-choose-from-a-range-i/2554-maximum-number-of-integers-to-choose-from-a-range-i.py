class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Convert banned list to a set for faster lookups
        banned_set = set(banned)
        
        count = 0
        current_sum = 0
        
        # Iterate through numbers from 1 to n
        for i in range(1, n + 1):
            if i not in banned_set:
                # Check if adding this number exceeds maxSum
                if current_sum + i <= maxSum:
                    current_sum += i
                    count += 1
                else:
                    break  # No need to continue if we exceed maxSum
        
        return count
