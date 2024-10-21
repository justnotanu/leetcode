class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # A set to store unique substrings
        unique_substrings = set()

        # Helper function for backtracking
        def backtrack(start: int) -> int:
            if start == len(s):
                return 0
            
            max_count = 0
            current_substring = ""
            
            # Try to create substrings starting from 'start'
            for end in range(start, len(s)):
                current_substring += s[end]
                
                # If the substring is unique, continue to the next part
                if current_substring not in unique_substrings:
                    unique_substrings.add(current_substring)
                    max_count = max(max_count, 1 + backtrack(end + 1))
                    unique_substrings.remove(current_substring)  # Backtrack
                
            return max_count

        return backtrack(0)
