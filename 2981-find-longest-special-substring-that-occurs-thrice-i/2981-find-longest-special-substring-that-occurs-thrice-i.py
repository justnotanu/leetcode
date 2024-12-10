class Solution:
    def maximumLength(self, s: str) -> int:
        max_length = -1
        n = len(s)

        # Iterate through all possible lengths of special substrings
        for length in range(1, n + 1):
            # Check for each character if it can form a special substring of this length
            for char in set(s):  # Use set to avoid duplicate checks for the same character
                special_substring = char * length
                count = 0
                
                # Count occurrences of the special substring
                for i in range(n - length + 1):
                    if s[i:i + length] == special_substring:
                        count += 1
                
                # Check if it occurs at least three times
                if count >= 3:
                    max_length = max(max_length, length)

        return max_length
        