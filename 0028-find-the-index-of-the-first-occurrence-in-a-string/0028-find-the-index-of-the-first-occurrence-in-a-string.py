class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is longer than haystack
        if len(needle) > len(haystack):
            return -1
        
        # Iterate through haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Compare substring with needle
            if haystack[i:i + len(needle)] == needle:
                return i  # Return the starting index
        
        return -1  # Return -1 if needle is not found
