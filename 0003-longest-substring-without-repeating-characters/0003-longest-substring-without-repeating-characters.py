class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Dictionary to store the last index of each character
        max_length = 0  # Variable to keep track of the maximum length of substring
        start = 0  # Left pointer for the sliding window

        for i, char in enumerate(s):
            # If the character is already in the map and its index is within the current window
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start pointer to one position right of the last occurrence
                start = char_index_map[char] + 1
            
            # Update or add the character's index to the map
            char_index_map[char] = i
            
            # Calculate the length of current substring and update max_length if needed
            max_length = max(max_length, i - start + 1)

        return max_length
