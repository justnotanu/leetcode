class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Convert nums to a set for O(1) lookups
        num_set = set(nums)
        max_streak = -1  # Initialize max streak to -1 (indicating no valid streak)

        # Iterate over each number in nums
        for num in nums:
            current_num = num
            streak_length = 0
            
            # While current_num is in num_set, continue squaring
            while current_num in num_set:
                streak_length += 1  # Increment streak length
                current_num *= current_num  # Square the current number
            
            # Check if we have a valid streak of at least length 2
            if streak_length > 1:
                max_streak = max(max_streak, streak_length)  # Update max_streak

        return max_streak
